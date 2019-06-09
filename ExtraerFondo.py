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
        numero_imagenes = 29
        fondo = self.imagen_original
        alpha = 0.1
        for i in range(numero_imagenes):
            if i < 8:
                namei = "im00000"+repr(i+2)+".jpg"
            else:
                namei = "im0000"+repr(i+2)+".jpg"
            alinear = self.ssd(namei)
            fondo = (1-alpha)*fondo+(alpha*alinear)
            #self.loop()
        cv2.imwrite("resultado4.jpg",fondo)
        img = cv2.imread("resultado4.jpg")
        cv2.imshow("resultado4.jpg",img)

    
    def ssd(self,namei):
        #leer la imagen i
        imageN = cv2.imread(namei,0)
        #self.showImage("ImagenN",imageN)
        rest = 99**99
        pos = []
        for y in range(imageN.shape[0]-self.mask.shape[0]):
            for x in range(imageN.shape[1]-self.mask.shape[1]):
                sum = 0
                tempCrop = imageN[int(y):int(y+self.mask.shape[0]),int(x):int(x+self.mask.shape[1])]
                sum = np.sum((tempCrop-self.mask)**2)
                if sum < rest :
                    rest = sum
                    pos = x,y
        desx =  self.cut[0] - pos[0]
        desy =  self.cut[1] - pos[1] 
        print("DESX: ",desx," DESY: ",desy)
        m = np.float32([[1,0,desx],[0,1,desy]])
        dst = cv2.warpAffine(imageN,m,(imageN.shape[1],imageN.shape[0]))
        return dst
         