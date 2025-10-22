import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Abrir imagen en color
img = Image.open("gatitos.jpg")
dato=0

# Convertir imagen a array NumPy
matriz = np.array(img)

# Obtener dimensiones originales
fil, col, canales = matriz.shape

# Crear nueva matriz vacía con dimensiones rotadas
# (intercambiamos filas y columnas)
matriz_rotada = np.zeros((col, fil, canales), dtype=np.uint8)

print("Ingresa (1) para rotar 90° la imagen")
print("Ingrese (2) para girar hacia la derecha")
print("Ingrese (3) para girar hacia la izquierda")
dato=int(input())
if (dato==1):
    for i in range(fil):
        for j in range(col):
            matriz_rotada[j][fil - 1 - i] = matriz[i][j]
    
    plt.imshow(matriz_rotada)
    plt.axis('off')
    plt.show()
else:
    if (dato==2):
        mitCol=col//2
        for i in range(fil):
            for j in range(col):
                aux=matriz[i][j]
                ind_op=mitCol-1-j
                matriz[i][j]=matriz[i][ind_op]
                matriz[i][ind_op]=aux
        plt.imshow(matriz)
        plt.axis('off')
        plt.show()
