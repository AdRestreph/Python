import albumentations as A
import numpy as np

IMG_SIZE = 128

transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.Rotate(limit=30, p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.RandomCrop(width=IMG_SIZE, height=IMG_SIZE, always_apply=True),
])

def augment_image(image):
    """Aplica transformaciones de aumentación a una imagen."""
    augmented = transform(image=image)
    return augmented['image']

def my_generator(generator):
    """Generador de imágenes aumentadas."""
    while True:
        data = next(generator)
        augmented_images = [augment_image(image) for image in data[0]]
        yield np.array(augmented_images), data[1]
