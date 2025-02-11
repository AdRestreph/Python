import os
import numpy as np
import matplotlib.pyplot as plt

def list_directory(path: str) -> list:
    """
    This function converts directory/files into a list of images.
    ----------
    path : [str] - directory path
    ----------
    return: [list]
    """
    files = os.listdir(path)
    return files

def modify_images(list_dir: list, path: str, save_path: str) -> str:
    """
    This function modifies the images in a directory and saves them in grayscale.
    ----------
    list_dir :  [list] - contains images in color
    path : [str] - directory path
    save_path : [str] - path to save grayscale images
    ----------
    return: [str] confirmation message
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for i in list_dir:
        image = plt.imread(os.path.join(path, i))
        image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        matrix_gray = np.array(image_gray)
        plt.imsave(os.path.join(save_path, f'gray_{i}'), matrix_gray, cmap='gray')

    message = print(f'Images converted to grayscale: {len(list_dir)}')
    return message

path = 'C:/Users/Usuario/Pictures/images/images_color/'
save_path = 'C:/Users/Usuario/Pictures/images/images_gray/'
list_dir = list_directory(path)
modify_images(list_dir, path, save_path)