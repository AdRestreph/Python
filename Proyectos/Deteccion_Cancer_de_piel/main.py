from dataset import load_data
from model import train_model
from predict import predict_image, evaluate_model
import tensorflow as tf
import os

# Cargar datos
(X_train, X_val, y_train, y_val), class_names = load_data()

# Entrenar modelo
model = train_model(X_train, y_train, X_val, y_val, len(class_names))

# Evaluar modelo
evaluate_model(model, X_val, y_val, class_names)

# Predecir una imagen específica
img_path = os.path.join('ruta/a/imagen.jpg')
predicted_disease = predict_image(model, img_path, class_names)
print(f'Predicted disease: {predicted_disease}')
