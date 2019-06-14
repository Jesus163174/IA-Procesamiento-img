# Calcular SSD
import numpy as np
import cv2




# imagenPrincipal = np.empty(shape = (15,15), dtype = int)#declar una matriz
imagenPrincipal = cv2.imread("C:/UPCH/OctavoCuatrimestre/IA/C1/A1/MateriaApoyo/1/mag.png",cv2.IMREAD_GRAYSCALE)
# mascara = np.empty(shape=(5,5), dtype= int )
# mascara = cv2.imread("C:/UPCH/OctavoCuatrimestre/IA/C1/A1/MateriaApoyo/1/magP.png",cv2.IMREAD_GRAYSCALE)
puntosSSD = np.empty(shape=())
ssd = 0
def main():
    # llenarMatrix()
    # funcname()
    # mostrar()
    init()
    # mascaraImagen()
    pass

#######
def init():
    # self.img = cv2.imread(self.nameimage,0) #read imagen of resource
    cv2.imshow("Original",imagenPrincipal) # show image
    eventMouseClick() # this method will wait a Click Event
    loop() # will wait finish the main
    pass

def eventMouseClick():
    cuadro = cv2.selectROI(imagenPrincipal)
    validated = validateMask(cuadro)
    mascara =createMask(cuadro[0],validated[0],cuadro[1],validated[1])
    cv2.imshow("MASK", mascara)
    pass
def validateMask(cuadro): #change method, una tupla no puede ser modificada
    
    x = cuadro[2]
    y = cuadro[3]
    if(x%2==0):
        x+=1
    if(y%2==0):
        y+=1
    return x,y
    pass

def createMask(self,xinitial,xfinish,yinitial,yfinish):
    return self.imagenPrincipal[int(yinitial):int(yinitial+yfinish),int(xinitial):int(xinitial+xfinish)]
    pass

def loop():
    cv2.waitKey(0)
    pass
######


def funcname():
    # print("imagen original: ")
    # print(imagenPrincipal)
    # print(imagenPrincipal.shape)
    # print("tamaño: ")
    # print(imagenPrincipal.size)

    print("mascara: ")
    print(mascara)
    print(mascara.shape)
    print(len(mascara) , "i")#filas
    print(len(mascara[0]))#columnas
    # print(mascara[234])
    print("tamaño: ")
    print(mascara.size)

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
    columna = len(imagenPrincipal[0]) 
    fila = len(imagenPrincipal)
    print( fila , columna)
    print("--------")
    columna = len(mascara[0]) 
    fila = len(mascara)
    print( fila , columna)
    #print (imagenPrincipal[7][7])
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
    
    for i in range(0,numeroFilaMascara+1):
        print("fila : " , i)
        x = 0
        for j in range(0,numeroColumanMascara+1):
            calcularSSD(i,j)
            # print("SSD: " )
            # print(ssd)
            x =x+1
            # print(x)
            pass
        print("SSD: " )
        print(ssd)
        pass
        # print("SSD: ")
        # print(ssd)
    pass

def calcularSSD(posicionI,posicionJ):
    global ssd
    ssd = 0
    aux = 0
    for i in range(posicionI,len(mascara) + posicionI):
        for j in range(posicionJ,len(mascara[0]) + posicionJ):
            ssd = ssd + (( mascara[i-posicionI][j-posicionJ] - imagenPrincipal[i][j] )**2)
            # aux = aux + 1
            pass
        pass
    # print("it : ", aux)
    pass

main()