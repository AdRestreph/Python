import numpy as np
import matplotlib.pyplot as plt

# Carga la imagen desde el directorio indicado
image = plt.imread("C:/Users/Usuario/Pictures/images/images_color/aguilar1.jpg")

# Convierte la imagen a escala de grises
image_gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])  # RGB a escala de grises

# Convierte la imagen en matriz usando NumPy
matrix_gray = np.array(image_gray)
matrix_color = np.array(image)
# Imprime las dimensiones de la imagen
print("Dimensiones en gris:", matrix_gray.shape)
#print("Dimensiones en color:", matrix_color.shape)

# Configuración para que NumPy imprima todos los valores de la matriz:

#np.set_printoptions(threshold=np.inf, suppress=True, linewidth=matrix_gray.shape[1] * 10)
#np.set_printoptions(threshold=np.inf, suppress=True, linewidth=matrix_color.shape[1] * 10)

# Imprime la matriz con valores completos

print("Matriz en gris:\n", matrix_gray)
print(type(matrix_gray))
#print("Matriz en color:\n", matrix_color)

# Muestra la imagen usando matplotlib
plt.imshow(image_gray, cmap='gray')
plt.axis("off")
plt.show()
