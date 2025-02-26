import numpy as np
import cv2
import tensorflow as tf
from dataset import preprocess_image
import os

def predict_image(model, img_path, class_names):
    """Realiza la predicción de una imagen."""
    img = np.expand_dims(preprocess_image(img_path), axis=0)
    pred = model.predict(img)
    pred_class = int(np.argmax(pred))
    return class_names[pred_class]

def evaluate_model(model, X_val, y_val, class_names):
    """Evalúa el modelo con imágenes de prueba y visualiza los resultados."""
    import matplotlib.pyplot as plt
    import random

    num_samples = 5
    random_indices = random.sample(range(len(X_val)), num_samples)
    sample_images = X_val[random_indices]
    sample_labels = y_val[random_indices]

    predictions = model.predict(sample_images)
    predicted_classes = np.argmax(predictions, axis=1)
    predicted_diseases = [class_names[i] for i in predicted_classes]

    true_classes = np.argmax(sample_labels, axis=1)
    accuracy = np.mean(predicted_classes == true_classes)

    plt.figure(figsize=(15, 5))
    for i in range(num_samples):
        plt.subplot(1, num_samples, i + 1)
        plt.imshow(cv2.cvtColor(sample_images[i], cv2.COLOR_BGR2RGB))
        title = f"True: {class_names[true_classes[i]]}\nPred: {predicted_diseases[i]}"
        plt.title(title)
        plt.axis('off')

    plt.suptitle(f"Accuracy: {accuracy:.2f}")
    plt.show()
