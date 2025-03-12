import numpy as np
import cv2
from scipy import ndimage

def degrees_img(image:np.ndarray) -> np.ndarray:
    """Rotates an image by a random angle."""
    angle = np.random.randint(0, 360)
    image_rotated = ndimage.rotate(image, angle, reshape=False)

    return np.array(image_rotated)

def gaussian_noise(image:np.ndarray) -> np.ndarray:
    """Añade ruido gaussiano a una imagen en escala de grises."""
    image = image.astype(np.float32)
    noise = np.random.normal(0, 0.1, image.shape)
    image_noise = np.clip(image + noise, 0, 1)

    return image_noise

def moved_img(image:np.ndarray) -> np.ndarray:
    """Moves the image out of the center by shifting it randomly."""
    height, width = image.shape[:2]
    shift_x = np.random.randint(-width // 4, width // 4)
    shift_y = np.random.randint(-height // 4, height // 4)

    translation_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    moved_image = cv2.warpAffine(image, translation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    return moved_image

