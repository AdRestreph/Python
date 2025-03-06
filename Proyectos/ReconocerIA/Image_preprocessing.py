import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

def resize_img(path:str, size:tuple) -> np.ndarray:
    """
    This function resizes an image to a specific size.
    ----------
    path : [str] - directory image/matrix
    size : [tuple] - new size of the image
    ----------
    return: [np.ndarray] - image/matrix resized
    """
    image = cv2.imread(path)
    image_resized = cv2.resize(image, size)
    matrix_resized = np.array(image_resized)

    return matrix_resized

def matrix_gray(image: np.ndarray) -> np.ndarray:
    """
    This function converts an image to grayscale and normalized the pixels.
    ----------
    path : [str] - directory image/matrix
    ----------
    return: [np.ndarray] - image/matrix in grayscale
    """
    image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    matrix_gray = np.array(image_gray)/255.0

    return matrix_gray

def main():
    path = 'C:/Users/Usuario/Pictures/images/images_'
    color_path = f'{path}color/'
    norm_path = f'{path}normalized/'
    list_dir = os.listdir(color_path)

    for img in list_dir:
        image = (color_path + img)
        image_resized = resize_img(image, size=(256, 256))
        image_gray = matrix_gray(image_resized)

        plt.imsave(norm_path + 'n_' + img, image_gray, cmap='gray')
        print(f'Image {img} resized, converted to grayscale, and normalized')

if __name__ == "__main__":
    main()

