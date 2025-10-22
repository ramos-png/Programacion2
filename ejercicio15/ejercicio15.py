import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
c=0
img=Image.open("gatitos.jpg") 
img_gris=ImageOps.grayscale(img)#Convierte la imagen a escala de grises
matriz=np.array(img_gris)#Convierte la imagen en una matriz 
fyc=matriz.shape #Obtiene las dimensiones de la imagen
fil=fyc[0]
col=fyc[1]
print(fil)
print(col)
mitCol=col//2
print (mitCol)
for i in range (fil):
    for x in range (mitCol):
        aux=matriz[i][x]
        ind_op=col-1-x
        matriz[i][x]=matriz[i][ind_op]
        matriz[i][ind_op]=aux
plt.imshow(matriz, cmap="grey")
plt.show()
