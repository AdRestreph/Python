import numpy as np
import matplotlib.pyplot as plt

# Carga la imagen desde el directorio indicado
image = plt.imread("C:/Users/Usuario/Pictures/aguilarB.jpg")

# Convierte la imagen a escala de grises
image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # RGB a escala de grises

# Convierte la imagen en matriz usando NumPy
matrix = np.array(image_gray)

# Imprime las dimensiones de la imagen
print("Dimensiones:", matrix.shape)

# Muestra la imagen usando matplotlib
plt.imshow(image_gray, cmap='gray')
plt.title("El mas bravo del mundo")
plt.axis("off")
plt.show()
