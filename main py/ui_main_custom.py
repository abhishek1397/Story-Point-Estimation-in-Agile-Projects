# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import time
import numpy as np
import pickle5 as pickle
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QMovie
import model
from ui_model_eval import Ui_MainWindow_model_eval
from ui_training_testing import Ui_MainWindow_training_testing
import webbrowser
import warnings
warnings.filterwarnings("ignore")

class Ui_MainWindow_custom(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 640)
        MainWindow.showMaximized() #############
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.dropshadow_layout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.dropshadow_layout_2.setContentsMargins(10, 10, 10, 10)
        self.dropshadow_layout_2.setSpacing(0)
        self.dropshadow_layout_2.setObjectName("dropshadow_layout_2")
        self.backgrd_frame = QtWidgets.QFrame(self.centralwidget)
        self.backgrd_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 29, 73, 255), stop:0.486425 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;\n"
"")
        self.backgrd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.backgrd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgrd_frame.setObjectName("backgrd_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.backgrd_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.backgrd_frame_2 = QtWidgets.QFrame(self.backgrd_frame)
        self.backgrd_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgrd_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgrd_frame_2.setObjectName("backgrd_frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.backgrd_frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.backgrd_frame_2)
        self.frame_title.setMinimumSize(QtCore.QSize(0, 55))
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMinimumSize(QtCore.QSize(0, 40))
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 52))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(30)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:rgb(255, 255, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_body = QtWidgets.QFrame(self.backgrd_frame_2)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_body)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_content = QtWidgets.QFrame(self.frame_body)
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_content)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_content)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_model_pretrain = QtWidgets.QPushButton(self.frame_2)
        self.folder="PretrainData"
        (self.pushButton_model_pretrain).clicked.connect(lambda:webbrowser.open(self.folder))#///////////////////////////////////
        self.pushButton_model_pretrain.setMinimumSize(QtCore.QSize(250, 250))
        self.pushButton_model_pretrain.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_model_pretrain.setFont(font)
        self.pushButton_model_pretrain.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(255, 170, 255);\n"
"    border-radius:125px;\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(255, 170, 255,150);\n"
"    border:5px sold rgb(255, 255, 0);\n"
"} ")
        self.pushButton_model_pretrain.setObjectName("pushButton_model_pretrain")
        self.horizontalLayout_2.addWidget(self.pushButton_model_pretrain)
        self.pushButton_model_train = QtWidgets.QPushButton(self.frame_2)
        (self.pushButton_model_train).clicked.connect(self.model_training_testing) ####################################333333333/////////
        self.pushButton_model_train.setMinimumSize(QtCore.QSize(250, 250))
        self.pushButton_model_train.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_model_train.setFont(font)
        self.pushButton_model_train.setStyleSheet("QPushButton{ \n"
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
        self.pushButton_model_train.setObjectName("pushButton_model_train")
        self.horizontalLayout_2.addWidget(self.pushButton_model_train)
        self.pushButton_model_eval = QtWidgets.QPushButton(self.frame_2)
        (self.pushButton_model_eval).clicked.connect(self.model_evaluation) ####################################333333333/////////
        self.pushButton_model_eval.setMinimumSize(QtCore.QSize(250, 250))
        self.pushButton_model_eval.setMaximumSize(QtCore.QSize(250, 250))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_model_eval.setFont(font)
        self.pushButton_model_eval.setStyleSheet("QPushButton{ \n"
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
        self.pushButton_model_eval.setObjectName("pushButton_model_eval")
        self.horizontalLayout_2.addWidget(self.pushButton_model_eval)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.frame_content)
        self.frame_exit_back = QtWidgets.QFrame(self.frame_body)
        self.frame_exit_back.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_exit_back.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_exit_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_exit_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_exit_back.setObjectName("frame_exit_back")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_exit_back)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_exit_back)
        (self.pushButton_back).clicked.connect(lambda:MainWindow.hide()) ####################################333333333//////////////////
        self.pushButton_back.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_back.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_back.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(182, 121, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(182, 121, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout.addWidget(self.pushButton_back)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_exit_back)
        (self.pushButton_exit).clicked.connect(exit) ##############3
        self.pushButton_exit.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButton_exit.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(182, 121, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(182, 121, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout.addWidget(self.pushButton_exit)
        self.verticalLayout_4.addWidget(self.frame_exit_back)
        self.verticalLayout.addWidget(self.frame_body)
        self.verticalLayout_3.addWidget(self.backgrd_frame_2)
        self.dropshadow_layout_2.addWidget(self.backgrd_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Training model with your own dataset"))
        self.pushButton_model_pretrain.setText(_translate("MainWindow", "Model\n"
"Pretraining"))
        self.pushButton_model_train.setText(_translate("MainWindow", "Model\n"
"Training and \n"
"Testing"))
        self.pushButton_model_eval.setText(_translate("MainWindow", "Model\n"
"Evaluation"))
        self.pushButton_back.setText(_translate("MainWindow", "Back to Home Window"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit Application"))
        
        
    
        

    def model_training_testing(self):
        self.MainWindow_model_training = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_training_testing()
        self.ui.setupUi(self.MainWindow_model_training)
        self.MainWindow_model_training.show()
        

    def model_evaluation(self):
        self.MainWindow_model_eval = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_model_eval()
        self.ui.setupUi(self.MainWindow_model_eval)
        self.MainWindow_model_eval.show()



'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_custom()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''