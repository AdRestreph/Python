import os
import numpy as np
import matplotlib.pyplot as plt

def directorys(save_path: str, list_grayscale_images:list) -> None:
    """
    This function save the images in the directory/folders.
    ----------
    save_path : [str] - directory path in which the images will be saved
    list_grayscale_images : [list] - list images/matrix in grayscale
    ----------
    return: [None]
    """
    for i in range(len(list_grayscale_images)):
        plt.imsave(save_path + f'gray_{str(i+1)}.png', list_grayscale_images[i], cmap='gray')

def modify_images( path: str) -> list:
    """
    This function modifies the images in a directory.
    ----------
    path : [str] - directory path
    save_path : [str] - path to save grayscale images
    ----------
    return: []
    """
    list_dir = os.listdir(path)
    grayscale_images = []

    for i in list_dir:
        image = plt.imread(os.path.join(path, i))
        image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        matrix_gray = np.array(image_gray)
        grayscale_images.append(matrix_gray)

    return grayscale_images

path = 'C:/Users/Usuario/Pictures/images/images_color/'
save_path = 'C:/Users/Usuario/Pictures/images/images_gray/'

directorys(save_path,modify_images(path))