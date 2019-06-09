import cv2
import numpy as np

class ExtraerFondo:
    def __init__(self,title,name_imagen_original):
        self.title = title
        self.name_imagen_original = name_imagen_original
        self.imagen_original = cv2.imread(self.name_imagen_original,0)
        self.showImage(self.title,self.imagen_original)
        self.mouseEvent()
        self.initExtraerFondo()
        self.loop()
    
    def showImage(self,title,imagen):
        cv2.imshow(title,imagen)
    
    def mouseEvent(self):
        self.cut = cv2.selectROI(self.imagen_original)
        self.validated = self.validateMask()
        self.mask = self.createMask(self.cut[0],self.validated[0],self.cut[1],self.validated[1])
        
    def validateMask(self):
        x = self.cut[2]
        y = self.cut[3]
        if(x%2==0):
            x+=1
        if(y%2==0):
            y+=1
        return x,y

    def createMask(self,xinitial,xfinish,yinitial,yfinish):
        return self.imagen_original[int(yinitial):int(yinitial+yfinish),int(xinitial):int(xinitial+xfinish)]

    def loop(self):
        cv2.waitKey(0)

    def initExtraerFondo(self):
        numero_imagenes = 5
        for i in range(numero_imagenes):
            namei = "im00000"+repr(i+2)+".jpg"
            print(namei)
            alinear = self.ssd(namei)
    
    def ssd(self,namei):
        return ""
         