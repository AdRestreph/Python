import numpy as np
import tensorflow as tf
import cv2
import sys

# Cargar el modelo entrenado
MODEL_PATH = "skin-disease-detection.h5"
model = tf.keras.models.load_model(MODEL_PATH)

# Clases del dataset HAM10000
CLASS_NAMES = ["Melanoma", "Nevus melanocítico", "Queratosis benigna", "Carcinoma basocelular",
               "Carcinoma de células escamosas", "Lesión vascular", "Dermatofibroma"]


def preprocess_image(image_path):
    """Carga y preprocesa la imagen para la predicción."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"No se pudo cargar la imagen: {image_path}")

    img = cv2.resize(img, (128, 128))  # Redimensionar
    img = img / 255.0  # Normalizar
    img = np.expand_dims(img, axis=0)  # Expandir dimensiones para el modelo
    return img


def predict(image_path):
    """Realiza la predicción en la imagen dada."""
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    class_index = np.argmax(prediction)  # Obtener índice de la clase con mayor probabilidad
    confidence = np.max(prediction)  # Obtener la confianza de la predicción

    print(f"Predicción: {CLASS_NAMES[class_index]} con una confianza del {confidence:.2%}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python predict_image.py <ruta_imagen>")
    else:
        image_path = sys.argv[1]
        predict(image_path)
