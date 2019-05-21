# Calcular SSD
import numpy as np
import cv2

imagenPrincipal = np.empty(shape = (15,15), dtype = int)#declar una matriz
mascara = np.empty(shape=(3,3), dtype= int )
puntosSSD = np.empty(shape=())
def main():
    llenarMatrix()
    funcname()
    mostrar()
    pass

def funcname():
    print(imagenPrincipal)
    pass

def llenarMatrix():
    global imagenPrincipal#hacer uso de una variable Global
    x = 0
    for i in range(0,15):
        for j in range(0,15):
            x += 1
            imagenPrincipal[i][j] = x 
            pass
        pass
    pass

def mostrar():
    '''  '''
    columna = len(imagenPrincipal)
    fila = len(imagenPrincipal[0]) 
    print( fila , columna)
    print (imagenPrincipal[7][7])
    pass

def mascaraImagen():#pasar parametro del tamaño de la imagen, mascara
    ''' En esta practica se usara una mascara de 5x5, para que la posicion 2,2 sea el centro y se pueda recuperar 
        un punto SSD.
            - Concer cuantas veces entra la mascara en la imagen:
                el numero de filas y columna de la imagen original se resta las filas y columna de la mascara
                filaImagenOriginal - filaMascara = numero de veces que entra la imagen la fila;
                columanImagenOriginal - columnaMascara = numero de veces que entra la imagen en columna;
    '''


    pass

main()