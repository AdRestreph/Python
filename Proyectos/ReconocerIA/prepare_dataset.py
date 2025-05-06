import os
import numpy as np
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from Proyectos.ReconocerIA.dataset_generation.image_preprocessing import resize_img, matrix_gray
from Proyectos.ReconocerIA.dataset_generation.data_augmentation import gaussian_noise, moved_img, degrees_img

load_dotenv()

def main():
    color_path = os.getenv('COLOR_PATH')
    norm_path = os.getenv('NORM_PATH')
    augmentation_path = os.getenv('AUGMENTATION_PATH')
    list_dir = os.listdir(color_path)

    for img in list_dir:
        image = (color_path + img)
        image_resized = resize_img(image, size=(255, 255))
        image_gray = matrix_gray(image_resized)

        plt.imsave(norm_path + 'n_' + img, image_gray, cmap='gray')
        print(f'Image {img} resized, converted to grayscale, and normalized')

        j = np.random.randint(1, 4)
        if j == 1:
            image_transformed = degrees_img(image_gray)
            output_path = os.path.join(augmentation_path, 'rot_' + img)
            print(f'Image {img} rotated')
        elif j == 2:
            image_transformed = gaussian_noise(image_gray)
            output_path = os.path.join(augmentation_path, 'gau_' + img)
            print(f'Image {img} with Gaussian noise')
        else:
            image_transformed = moved_img(image_gray)
            output_path = os.path.join(augmentation_path, 'mov_' + img)
            print(f'Image {img} moved')

        plt.imsave(output_path.replace('.jpg', '.png'), np.clip(image_transformed, 0, 1), cmap='gray', format='png')

if __name__ == "__main__":
    main()