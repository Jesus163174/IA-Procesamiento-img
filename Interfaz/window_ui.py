# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1258, 472)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QtCore.QSize(1258, 472))
        self.scroll_image_before = QtWidgets.QScrollArea(Dialog)
        self.scroll_image_before.setGeometry(QtCore.QRect(40, 50, 521, 401))
        self.scroll_image_before.setWidgetResizable(True)
        self.scroll_image_before.setObjectName("scroll_image_before")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 519, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_image_before.setWidget(self.scrollAreaWidgetContents)
        # self.button_fit = QtWidgets.QPushButton(Dialog)
        # self.button_fit.setGeometry(QtCore.QRect(40, 20, 75, 23))
        #self.button_fit.setObjectName("button_fit")
        self.scroll_image_after = QtWidgets.QScrollArea(Dialog)
        self.scroll_image_after.setGeometry(QtCore.QRect(680, 50, 521, 401))
        self.scroll_image_after.setWidgetResizable(True)
        self.scroll_image_after.setObjectName("scroll_image_after")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 519, 399))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scroll_image_after.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(580, 160, 91, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_equal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        # self.button_equal.setFont(font)
        # self.button_equal.setObjectName("button_equal")
        self.verticalLayout.addWidget(self.button_equal)
        self.button_different = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        # self.button_different.setFont(font)
        # self.button_different.setObjectName("button_different")
        self.verticalLayout.addWidget(self.button_different)
        # self.button_fit_after = QtWidgets.QPushButton(Dialog)
        # self.button_fit_after.setGeometry(QtCore.QRect(1120, 20, 75, 23))
        # # self.button_fit_after.setObjectName("button_fit_after")
        # self.button_export = QtWidgets.QPushButton(Dialog)
        # self.button_export.setGeometry(QtCore.QRect(1030, 20, 75, 23))
        # self.button_export.setObjectName("button_export")
        self.button_select = QtWidgets.QPushButton(Dialog)
        self.button_select.setGeometry(QtCore.QRect(130, 20, 89, 23))
        self.button_select.setObjectName("button_select")
        # self.check_gray = QtWidgets.QCheckBox(Dialog)
        # self.check_gray.setGeometry(QtCore.QRect(590, 340, 70, 17))
        # self.check_gray.setObjectName("check_gray")
        # self.check_saturar = QtWidgets.QCheckBox(Dialog)
        # self.check_saturar.setGeometry(QtCore.QRect(590, 370, 70, 17))
        # self.check_saturar.setObjectName("check_saturar")
        # self.check_mapear = QtWidgets.QCheckBox(Dialog)
        # self.check_mapear.setGeometry(QtCore.QRect(590, 400, 70, 17))
        # self.check_mapear.setObjectName("check_mapear")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image-Process"))
        # self.button_fit.setText(_translate("Dialog", "Fit To Box"))
        # self.button_equal.setText(_translate("Dialog", "α=γ"))
        # self.button_different.setText(_translate("Dialog", "α!=γ"))
        # self.button_fit_after.setText(_translate("Dialog", "Fit To Box"))
        # self.button_export.setText(_translate("Dialog", "Export Image"))
        self.button_select.setText(_translate("Dialog", "Import Image"))
        # self.check_gray.setText(_translate("Dialog", "GrayScale"))
        # self.check_saturar.setText(_translate("Dialog", "Saturar"))
        # self.check_mapear.setText(_translate("Dialog", "Mapear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

