import os
import numpy as np
import pandas as pd
import cv2
import kagglehub
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf

# Descargar el dataset
path = kagglehub.dataset_download("kmader/skin-cancer-mnist-ham10000")
DATA_DIR = path
IMAGES_DIR_1 = os.path.join(DATA_DIR, 'HAM10000_images_part_1')
IMAGES_DIR_2 = os.path.join(DATA_DIR, 'HAM10000_images_part_2')
METADATA_FILE = os.path.join(DATA_DIR, 'HAM10000_metadata.csv')

# Cargar metadatos
df = pd.read_csv(METADATA_FILE, usecols=['image_id', 'dx'])

IMG_SIZE = 128

def preprocess_image(img_path):
    """Carga y preprocesa una imagen."""
    try:
        img = cv2.imread(img_path)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = img / 255.0
        return img
    except Exception as e:
        print(f'Error procesando imagen {img_path}: {e}')
        return None

# Cargar imágenes y etiquetas
def load_data():
    images, labels = [], []
    for _, row in df.iterrows():
        image_id = row['image_id']
        image_path1 = os.path.join(IMAGES_DIR_1, image_id + '.jpg')
        image_path2 = os.path.join(IMAGES_DIR_2, image_id + '.jpg')

        if os.path.exists(image_path1):
            img = preprocess_image(image_path1)
        elif os.path.exists(image_path2):
            img = preprocess_image(image_path2)
        else:
            print(f"Imagen no encontrada: {image_id}")
            continue

        if img is not None:
            images.append(img)
            labels.append(row['dx'])

    images = np.array(images, dtype=np.float32)
    labels = np.array(labels)

    le = LabelEncoder()
    labels = le.fit_transform(labels)
    labels = tf.keras.utils.to_categorical(labels, num_classes=len(le.classes_))

    return train_test_split(images, labels, test_size=0.2, random_state=42), le.classes_
