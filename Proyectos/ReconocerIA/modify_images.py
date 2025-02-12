import os
import numpy as np
import matplotlib.pyplot as plt

def directorys(save_path: str, iterable:int, matrix:set) -> list:
    """
    This function save the images in the directory/folders.
    ----------
    path : [str] - directory path
    ----------
    return: [list]
    """

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    plt.imsave(os.path.join(save_path, f'gray_{iterable}'), matrix, cmap='gray')
    message = print(f'Images converted to grayscale: {iterable}')

    return message

def modify_images( path: str,save_path: str) -> None:
    """
    This function modifies the images in a directory and saves them in grayscale.
    ----------
    list_dir :  [list] - contains images in color
    path : [str] - directory path
    save_path : [str] - path to save grayscale images
    ----------
    return: [str] confirmation message
    """
    list_dir = os.listdir(path)

    for i in list_dir:
        image = plt.imread(os.path.join(path, i))
        image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        matrix_gray = np.array(image_gray)
        directorys(save_path, i, matrix_gray)

path = 'C:/Users/Usuario/Pictures/images/images_color/'
save_path = 'C:/Users/Usuario/Pictures/images/images_gray/'
modify_images(path, save_path)
