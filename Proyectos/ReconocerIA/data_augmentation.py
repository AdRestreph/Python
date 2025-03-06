import os
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
import cv2

def degrees_img(path: str) -> np.ndarray:
    """Rotates an image by a random angle."""
    image = plt.imread(path)
    angle = np.random.randint(0, 360)
    image_rotated = ndimage.rotate(image, angle, reshape=False)

    return np.array(image_rotated)

def gaussian_noise(path: str) -> np.ndarray:
    """Añade ruido gaussiano a una imagen en escala de grises."""
    image = plt.imread(path).astype(np.float32)
    noise = np.random.normal(0, 0.001, image.shape)
    image_noise = np.clip(image + noise, 0, 1)

    return image_noise

def moved_img(path: str) -> np.ndarray:
    """Moves the image out of the center by shifting it randomly."""
    image = plt.imread(path)
    height, width = image.shape[:2]
    shift_x = np.random.randint(-width // 4, width // 4)
    shift_y = np.random.randint(-height // 4, height // 4)

    translation_matrix = np.float32([[1, 0, shift_x], [0, 1, shift_y]])
    moved_image = cv2.warpAffine(image, translation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    return moved_image

def main():
    path = 'C:/Users/Usuario/Pictures/images/images_'
    normalized_path = os.path.join(path + 'normalized/')
    augmentation_path = os.path.join(path + 'augmented/')
    list_dir = os.listdir(normalized_path)

    image_with_noise = gaussian_noise('C:/Users/Usuario/Pictures/images/images_color/1.jpg')
    plt.imshow(image_with_noise, cmap='gray')
    plt.title('Image with Gaussian Noise')
    plt.axis('off')
    plt.show()

    for img in list_dir:
        image_path = os.path.join(normalized_path + img)
        j = np.random.randint(1, 4)

        if j == 1:
            image_transformed = degrees_img(image_path)
            output_path = os.path.join(augmentation_path, 'r_' + img)
            print(f'Image {img} rotated')
        elif j == 2:
            image_transformed = gaussian_noise(image_path)
            output_path = os.path.join(augmentation_path, 'gau_' + img)
            print(f'Image {img} with Gaussian noise')
        else:
            image_transformed = moved_img(image_path)
            output_path = os.path.join(augmentation_path, 'm_' + img)
            print(f'Image {img} moved')

        plt.imsave(output_path, image_transformed, cmap='gray')

if __name__ == "__main__":
    main()
