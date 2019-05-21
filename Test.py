# Calcular SSD
import numpy as np
import cv2

imagenPrincipal = np.empty(shape = (15,15), dtype = int)#declar una matriz
mascara = np.empty(shape=(5,5), dtype= int )
puntosSSD = np.empty(shape=())
ssd = 0
def main():
    llenarMatrix()
    funcname()
    # mostrar()
    mascaraImagen()
    pass

def funcname():
    print("imagen original: ")
    print(imagenPrincipal)
    print("mascara: ")
    print(mascara)
    pass

def llenarMatrix():
    global imagenPrincipal#hacer uso de una variable Global
    x = 0
    for i in range(0,len(imagenPrincipal)):
        for j in range(0,len(imagenPrincipal[0])):
            x += 1
            imagenPrincipal[i][j] = x 
            pass
        pass
        ''' llenar la mascara '''
    f = 0
    for i in range(10,len(imagenPrincipal)):
        c=0
        for j in range(10,len(imagenPrincipal[0])):
            mascara[f][c] = imagenPrincipal[i][j]
            c = c + 1
            pass
        f = f + 1
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
    numeroFilaMascara = len(imagenPrincipal) - len(mascara)#Calcular el numero de veces que entra la mascara en las filas de la imagenPrincipal
    numeroColumanMascara = len(imagenPrincipal[0])- len(mascara[0])#Calcular el numero de veces que entra la mascara en las columna de la imagenPrincipal
    #filaMascara = len(imagenPrincipal) - numeroColumanMascara #obtener el numero de pixes que se deben tomar en fila
    #columnaMascara = len(imagenPrincipal[0]) - numeroColumanMascara #obtener el numero de pixes que se deben tomar en columna
    print(numeroFilaMascara,numeroColumanMascara)#, filaMascara, columnaMascara)
    x = 0
    for i in range(0,numeroFilaMascara+1):
        for j in range(0,numeroColumanMascara+1):
            calcularSSD(i,j)
            print("SSD: " )
            print(ssd)
            x =x+1
            print(x)
            pass
        pass
        # print("SSD: ")
        # print(ssd)
    pass

def calcularSSD(posicionI,posicionJ):
    global ssd
    ssd = 0
    for i in range(posicionI,len(mascara) + posicionI):
        for j in range(posicionJ,len(mascara[0]) + posicionJ):
            ssd = ssd + (( mascara[i-posicionI][j-posicionJ] - imagenPrincipal[i][j] )**2)
            # aux = aux + 1
            pass
        pass

    pass

main()