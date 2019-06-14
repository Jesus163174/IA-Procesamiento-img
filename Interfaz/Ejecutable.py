from window_ui import *
from popup import PopUp
from popup_b import PopUpB
from ImageP import ImageP

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        # self.button_equal.clicked.connect(self.dialogValue)
        # self.button_different.clicked.connect(self.dialogValue_b)
        self.button_select.clicked.connect(self.selectImage)
        #self.button_fit.clicked.connect(self.fitImage)
        # self.button_fit_after.clicked.connect(self.fitImageAfter)
        # self.button_export.clicked.connect(self.saveFileDialog)
        # self.check_gray.clicked.connect(self.imageGray)
    
    # def dialogValue(self):
    #     popup = PopUp()
    #     number=False
    #     while not (number):
    #         number=True
    #         if popup.exec_():
    #             print(popup.text_alfa.text())
    #             print(popup.text_gamma.text())
    #             number=True
    #             try:
    #                 alpha = float(popup.text_alfa.text())
    #                 gamma=float(popup.text_gamma.text())
    #                 self.imageProcess(alpha,gamma)
    #             except ValueError:
    #                 number=False
        
    
    # def dialogValue_b(self):
    #     popupb = PopUpB()
    #     number=False
    #     while not (number):
    #         number=True
    #         if popupb.exec_():
    #             number=True
    #             try:
    #                 alpha_r = float(popupb.text_alfa_r.text())
    #                 gamma_r=float(popupb.text_gamma_r.text())
    #                 alpha_g = float(popupb.text_alfa_g.text())
    #                 gamma_g=float(popupb.text_gamma_g.text())
    #                 alpha_b = float(popupb.text_alfa_b.text())
    #                 gamma_b=float(popupb.text_gamma_b.text())
    #                 val=([alpha_b,gamma_b],[alpha_g,gamma_g],[alpha_r,gamma_r])
    #                 self.imageProcess_b(val)
    #             except ValueError:
    #                 number=False
        

    # def putImage(self,image_):
    #     size = image_.shape
    #     step = image_.size / size[0]
    #     qformat = QtGui.QImage.Format_Indexed8
    #     if len(size) == 3:
    #         if size[2] == 4:
    #             qformat = QtGui.QImage.Format_RGBA8888
    #         else:
    #             qformat = QtGui.QImage.Format_RGB888
    #     img = QtGui.QImage(image_, size[1], size[0], step, qformat)
    #     img = img.rgbSwapped()
    #     aux.imageOnScreen=img
    #     imageLabel = QtWidgets.QLabel()
    #     pixmap = QtGui.QPixmap.fromImage(img)    
    #     imageLabel.setPixmap(pixmap)
    #     self.scroll_image_after.setBackgroundRole(QtGui.QPalette.Dark)
    #     self.scroll_image_after.setWidget(imageLabel)

    # def imageProcess(self, alfa, gamma):
    #     image_=aux.processChange(alfa, gamma,self.check_gray.isChecked(),self.check_saturar.isChecked(),self.check_mapear.isChecked())
    #     self.putImage(image_)
    
    # def imageProcess_b(self, val):      
    #     image_=aux.processChange_b(val,self.check_gray.isChecked(),self.check_saturar.isChecked(),self.check_mapear.isChecked())
    #     self.putImage(image_)
         
    # def imageGray(self):
    #     if self.check_gray.isChecked():
    #         self.button_different.setDisabled(True)
    #     else:
    #         self.button_different.setDisabled(False)

    def selectImage(self):
        imageLabel = QtWidgets.QLabel()
        image , _ = QtWidgets.QFileDialog.getOpenFileName(None,
        'Select Image', '', "Image files (*.jpg *.png *.jpeg)")    
        if image:
            aux.setImage(image)
            pixmap = QtGui.QPixmap(image)    
            imageLabel.setPixmap(pixmap)
            self.scroll_image_before.setBackgroundRole(QtGui.QPalette.Dark)
            self.scroll_image_before.setWidget(imageLabel)   

    # def fitImage(self):
    #     imageLabel = QtWidgets.QLabel()   
    #     image = QtGui.QImage(aux.image)
    #     if image:
    #         pixmap = QtGui.QPixmap(image)    
    #         pixmap = pixmap.scaled(imageLabel.width(),imageLabel.height(),QtCore.Qt.KeepAspectRatio)
    #         imageLabel.setPixmap(pixmap)
    #         imageLabel.setAlignment(QtCore.Qt.AlignCenter)
    #         self.scroll_image_before.setBackgroundRole(QtGui.QPalette.Dark)
    #         self.scroll_image_before.setWidget(imageLabel)  
    
    # def fitImageAfter(self):
    #     imageLabel = QtWidgets.QLabel()   
    #     image = QtGui.QImage(aux.imageOnScreen)
    #     if image:
    #         pixmap = QtGui.QPixmap(image)    
    #         pixmap = pixmap.scaled(imageLabel.width(),imageLabel.height(),QtCore.Qt.KeepAspectRatio)
    #         imageLabel.setPixmap(pixmap)
    #         imageLabel.setAlignment(QtCore.Qt.AlignCenter) 
    #         self.scroll_image_after.setBackgroundRole(QtGui.QPalette.Dark)
    #         self.scroll_image_after.setWidget(imageLabel)    
    
    # def saveFileDialog(self):
    #     options = QtWidgets.QFileDialog.Options()
    #     options |= QtWidgets.QFileDialog.DontUseNativeDialog
    #     fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","jpg (*.jpg)", options=options)
    #     if fileName and aux.imageOnScreen:
    #         aux.exportImage(fileName)
            

aux = ImageP()   
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
