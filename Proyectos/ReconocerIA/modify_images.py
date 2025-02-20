import os
import numpy as np
import matplotlib.pyplot as plt

def matrix_gray(path:str) -> np.ndarray:
    """
    This function converts an image to grayscale.
    ----------
    path : [str] - directory image/matrix
    ----------
    return: [np.ndarray] - image/matrix in grayscale
    """
    image = plt.imread(path)
    image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    matrix_gray = np.array(image_gray)

    return matrix_gray

def main():
    path = 'C:/Users/Usuario/Pictures/images/images_'
    color_path = f'{path}color/'
    gray_path = f'{path}gray/'
    list_dir = os.listdir(color_path)
    for img in list_dir:
        matrix = matrix_gray(color_path + img)
        plt.imsave(gray_path + 'gray_' + img, matrix, cmap= plt.get_cmap('gray'))


if __name__ == "__main__":
    main()

