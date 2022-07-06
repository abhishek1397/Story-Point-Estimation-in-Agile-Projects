# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#original 
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main_calst import Ui_MainWindow_calst
from ui_main_detail_dataset import Ui_MainWindow_dataset_details
from ui_main_custom import Ui_MainWindow_custom

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1129, 445)
        MainWindow.showMaximized() #############
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.drop_shadow_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName("drop_shadow_layout")
        self.drop_shadow_frame = QtWidgets.QFrame(self.centralwidget)
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.147727 rgba(28, 29, 73, 255), stop:0.5209 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;")
        self.drop_shadow_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drop_shadow_frame.setObjectName("drop_shadow_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(self.drop_shadow_frame)
        self.title.setMaximumSize(QtCore.QSize(16777215, 50))
        self.title.setStyleSheet("background-color:none;")
        self.title.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.title)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_title = QtWidgets.QFrame(self.title)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(14)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(30)
        font.setItalic(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:rgb(255, 255, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addWidget(self.frame_title, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.title)
        self.content = QtWidgets.QFrame(self.drop_shadow_frame)
        self.content.setMinimumSize(QtCore.QSize(15, 15))
        self.content.setStyleSheet("background-color:none;")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.content)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 150, 981, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dataset_details_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.dataset_details_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dataset_details_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataset_details_2.setObjectName("dataset_details_2")
        self.pushButton_dataset_details = QtWidgets.QPushButton(self.dataset_details_2)
        (self.pushButton_dataset_details).clicked.connect(self.dataset_details_fxn) ####################################333333333/////////////////
        self.pushButton_dataset_details.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.pushButton_dataset_details.setMinimumSize(QtCore.QSize(250, 250))
        self.pushButton_dataset_details.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_dataset_details.setFont(font)
        self.pushButton_dataset_details.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(255, 170, 255);\n"
"    border-radius:125px;\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 170, 255,150);\n"
"    border:5px sold rgb(255, 255, 0);\n"
"} ")
        self.pushButton_dataset_details.setObjectName("pushButton_dataset_details")
        self.Cal_SP = QtWidgets.QFrame(self.dataset_details_2)
        self.Cal_SP.setGeometry(QtCore.QRect(370, 0, 250, 250))
        self.Cal_SP.setMinimumSize(QtCore.QSize(250, 250))
        self.Cal_SP.setMaximumSize(QtCore.QSize(250, 250))
        self.Cal_SP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cal_SP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Cal_SP.setObjectName("Cal_SP")
        self.pushButton_cal_sp = QtWidgets.QPushButton(self.Cal_SP)
        (self.pushButton_cal_sp).clicked.connect(self.calSP) ####################################333333333///////////////////////////
        self.pushButton_cal_sp.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.pushButton_cal_sp.setMinimumSize(QtCore.QSize(250, 250))
        self.pushButton_cal_sp.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_cal_sp.setFont(font)
        self.pushButton_cal_sp.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(255, 170, 0);\n"
"    border-radius:125px;\n"
"\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    \n"
"    \n"
"    background-color: rgba(255, 170, 0, 175);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} ")
        self.pushButton_cal_sp.setObjectName("pushButton_cal_sp")
        self.Custom_training = QtWidgets.QFrame(self.dataset_details_2)
        self.Custom_training.setGeometry(QtCore.QRect(730, 0, 250, 250))
        self.Custom_training.setMinimumSize(QtCore.QSize(250, 250))
        self.Custom_training.setMaximumSize(QtCore.QSize(250, 250))
        self.Custom_training.setStyleSheet("")
        self.Custom_training.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Custom_training.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Custom_training.setObjectName("Custom_training")
        self.pushButton_cus_train = QtWidgets.QPushButton(self.Custom_training)
        (self.pushButton_cus_train ).clicked.connect(self.custom_training_fxn) ####################################333333333///////////////////////////
        self.pushButton_cus_train.setGeometry(QtCore.QRect(0, 0, 250, 250))
        self.pushButton_cus_train.setMinimumSize(QtCore.QSize(250, 250))
        self.pushButton_cus_train.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_cus_train.setFont(font)
        self.pushButton_cus_train.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color:rgb(255, 0, 255);\n"
"    border-radius:125px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 0, 255, 150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
" \n"
"")
        self.pushButton_cus_train.setObjectName("pushButton_cus_train")
        self.horizontalLayout_3.addWidget(self.dataset_details_2)
        self.verticalLayout.addWidget(self.content)
        self.credit = QtWidgets.QFrame(self.drop_shadow_frame)
        self.credit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.credit.setStyleSheet("background-color:none;")
        self.credit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.credit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.credit.setObjectName("credit")
        self.pushButton_exit = QtWidgets.QPushButton(self.credit)
        (self.pushButton_exit).clicked.connect(exit) ##############3
        self.pushButton_exit.setGeometry(QtCore.QRect(620, 0, 75, 23))
        self.pushButton_exit.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(170, 255, 127);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(170, 255, 127,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} ")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout.addWidget(self.credit)
        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Story Point Estimation"))
        self.pushButton_dataset_details.setText(_translate("MainWindow", "View\n"
"Dataset\n"
"Details"))
        self.pushButton_cal_sp.setText(_translate("MainWindow", "Calculate \n"
"Story Point"))
        self.pushButton_cus_train.setText(_translate("MainWindow", "Custom\n"
"Training"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))

    def calSP(self):                                                        #  to call calculate story point window call from line 123
            self.calSP_MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_calst()
            self.ui.setupUi(self.calSP_MainWindow)
            self.calSP_MainWindow.show()
            
    def dataset_details_fxn(self):                                                  #####################################
            self.dataset_details_MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_dataset_details()
            self.ui.setupUi(self.dataset_details_MainWindow)
            self.dataset_details_MainWindow.show()
            
    def custom_training_fxn(self):
            self.MainWindow_training = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_custom()
            self.ui.setupUi(self.MainWindow_training)
            self.MainWindow_training.show()
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
