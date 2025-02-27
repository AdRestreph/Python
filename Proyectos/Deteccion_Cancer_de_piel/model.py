import tensorflow as tf
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.optimizers import Adam
import augmentation


def create_model(input_shape, num_classes):
    """Crea y devuelve un modelo CNN."""
    model = Sequential([
        Conv2D(16, (3, 3), activation='relu', input_shape=input_shape),
        MaxPooling2D((2, 2)),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])
    return model


def train_model(X_train, y_train, X_val, y_val, num_classes):
    """Entrena el modelo y lo guarda."""
    input_shape = (128, 128, 3)
    model = create_model(input_shape, num_classes)

    batch_size = 32
    train_datagen = tf.keras.preprocessing.image.ImageDataGenerator()
    val_datagen = tf.keras.preprocessing.image.ImageDataGenerator()

    train_generator = train_datagen.flow(X_train, y_train, batch_size=batch_size)
    val_generator = val_datagen.flow(X_val, y_val, batch_size=batch_size)

    augmented_train_generator = augmentation.my_generator(train_generator)

    model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

    early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
    lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, min_lr=0.00001)

    model.fit(augmented_train_generator,
              steps_per_epoch=len(X_train) // batch_size,
              epochs=35,
              validation_data=val_generator,
              validation_steps=len(X_val) // batch_size,
              callbacks=[early_stopping, lr_scheduler])

    model.save('skin-disease-detection.h5')
    return model
