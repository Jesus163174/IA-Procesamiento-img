import cv2
import numpy as np
class Imagen:
    def __init__(self,nameimage,title):
        self.nameimage = nameimage
        self.title = title
        x = cv2.imread("logo2.jpg",0)
        cv2.imshow("desplazada ",x)
    
    def init(self):
        self.img = cv2.imread(self.nameimage,0) #read imagen of resource
        cv2.imshow(self.title,self.img) # show image
        self.eventMouseClick() # this method will wait a Click Event
        self.loop() # will wait finish the main

    def eventMouseClick(self):
        self.cuadro = cv2.selectROI(self.img)
        self.validated = self.validateMask()
        self.mCrop = self.createMask(self.cuadro[0],self.validated[0],self.cuadro[1],self.validated[1])
        Displacement(self.mCrop,self.cuadro)

    def validateMask(self): #change method, una tupla no puede ser modificada
        x = self.cuadro[2]
        y = self.cuadro[3]
        if(x%2==0):
            x+=1
        if(y%2==0):
            y+=1
        return x,y

    def createMask(self,xinitial,xfinish,yinitial,yfinish):
        return self.img[int(yinitial):int(yinitial+yfinish),int(xinitial):int(xinitial+xfinish)]

    def loop(self):
        cv2.waitKey(0)
    
class Displacement:

    def __init__(self,mask,cuadrado):
        self.mask = mask
        self.cuadrado = cuadrado
        self.img = cv2.imread("logo2.jpg",0)
        cv2.imshow("desplazada ",self.img)
        self.initSSD()
    
    def initSSD(self): #ssd
        rest = 99**9
        pos  = []
        for y in range(self.img.shape[0]-self.mask.shape[0]):
            for x in range(self.img.shape[1]-self.mask.shape[1]):
                sum = 0
                tempCrop = self.img[int(y):int(y+self.mask.shape[0]),int(x):int(x+self.mask.shape[1])]
                sum = np.sum((tempCrop-self.mask)**2)
                if sum < rest :
                    rest = sum
                    pos = x,y

        desx =  self.cuadrado[0] - pos[0]
        desy =  self.cuadrado[1] - pos[1] 

        m = np.float32([[1,0,desx],[0,1,desy]])
        dst = cv2.warpAffine(self.img,m,(self.img.shape[1],self.img.shape[0]))
        
        cv2.imwrite("resultado.jpg",dst)
        cv2.imshow("Resultado",dst)


       
        
            
                
               
                

        