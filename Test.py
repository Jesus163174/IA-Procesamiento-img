# Calcular SSD
import numpy as np
import cv2
#mi rama
imagenPrincipal = np.empty(shape = (15,18), dtype = int)#declar una matriz
mascara = np.empty(shape=(5,5), dtype= int )
puntosSSD = np.empty(shape=())
def main():
    # llenarMatrix()
    funcname()
    mostrar()
    mascaraImagen()
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
    fila = len(imagenPrincipal)
    columna = len(imagenPrincipal[0]) 
    print( fila , columna)
    print (imagenPrincipal[7][7])
    pass

def mascaraImagen():#pasar parametro del tamaño de la imagen, mascara
    global mascara #hacer uso de la variable global
    ''' En esta practica se usara una mascara de 5x5, para que la posicion 2,2 sea el centro y se pueda recuperar 
        un punto SSD.
            - Concer cuantas veces entra la mascara en la imagen:
                el numero de filas y columna de la imagen original se resta las filas y columna de la mascara
                filaImagenOriginal - filaMascara = numero de veces que entra la imagen la fila;
                columanImagenOriginal - columnaMascara = numero de veces que entra la imagen en columna;
    '''
    filaMascara = len(imagenPrincipal) - len(mascara)#Calcular el numero de veces que entra la mascara en las filas de la imagenPrincipal
    columanMascara = len(imagenPrincipal[0])- len(mascara[0])#Calcular el numero de veces que entra la mascara en las columna de la imagenPrincipal
    print(filaMascara,columanMascara)
    
    # for i in range(0,filaMascara):
    #     for j in range(0,columanMascara):
    #         calcularSSD()
    #         pass
    #     pass

    pass

def calcularSSD():

    for i in range(0,len(mascara)):
        pass

    pass

main()