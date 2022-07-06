# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import re
import glob
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from pandas_ml import ConfusionMatrix
import itertools
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import train_test_algo

class Ui_MainWindow_training_testing(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 681)
        MainWindow.showMaximized() #############
        self.data_trained_validation=0
        font = QtGui.QFont()
        font.setPointSize(82)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.backgrd_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.backgrd_frame)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_title.setFont(font)
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
        self.label_title.setStyleSheet("color: rgb(255, 255, 0);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_body = QtWidgets.QFrame(self.backgrd_frame)
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.label = QtWidgets.QLabel(self.frame_body)
        self.label.setGeometry(QtCore.QRect(461, 78, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(170, 255, 127);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.plainTextEdit_k_value = QtWidgets.QTextEdit(self.frame_body)
        self.plainTextEdit_k_value.setGeometry(QtCore.QRect(691, 90, 104, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit_k_value.setFont(font)
        self.plainTextEdit_k_value.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.plainTextEdit_k_value.setStyleSheet("QTextEdit{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color:rgb(255, 170, 255);\n"
"}\n"
" \n"
"")
        self.plainTextEdit_k_value.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_k_value.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_k_value.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.plainTextEdit_k_value.setObjectName("plainTextEdit_k_value")
        self.pushButton_hint = QtWidgets.QPushButton(self.frame_body)
        (self.pushButton_hint).clicked.connect(self.K_hint) ####################################333
        self.pushButton_hint.setGeometry(QtCore.QRect(830, 95, 71, 21))
        self.pushButton_hint.setToolTip("")
        self.pushButton_hint.setStyleSheet("QPushButton{ \n"
"    border:rgb(0, 255, 127);\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 255, 127,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_hint.setObjectName("pushButton_hint")
        self.pushButton_training = QtWidgets.QPushButton(self.frame_body)
        (self.pushButton_training).clicked.connect(self.model_training_fxn) ####################################333
        self.pushButton_training.setGeometry(QtCore.QRect(538, 190, 261, 63))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_training.setFont(font)
        self.pushButton_training.setStyleSheet("\n"
"QPushButton{ \n"
"    border:rgb(0, 255, 127);\n"
"    background-color:rgb(128, 200, 126);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 255, 127,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_training.setObjectName("pushButton_training")
        '''self.pushButton_train_plot = QtWidgets.QPushButton(self.frame_body)
        (self.pushButton_train_plot).clicked.connect(lambda:self.model_training_plot(plot_select=1))############################################################33
        self.pushButton_train_plot.setGeometry(QtCore.QRect(403, 310, 220, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_train_plot.setFont(font)
        self.pushButton_train_plot.setStyleSheet("QPushButton{ \n"
"    border:rgb(0, 255, 127);\n"
"    background-color:rgb(190, 255, 155);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(190, 255, 155,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} ")
        self.pushButton_train_plot.setObjectName("pushButton_train_plot")
        self.pushButton_test_plot = QtWidgets.QPushButton(self.frame_body)
        (self.pushButton_test_plot).clicked.connect(lambda:self.model_training_plot(plot_select=2))############################################################33
        self.pushButton_test_plot.setGeometry(QtCore.QRect(737, 310, 220, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_test_plot.setFont(font)
        self.pushButton_test_plot.setStyleSheet("QPushButton{ \n"
"    border:rgb(0, 255, 127);\n"
"    background-color:rgb(190, 255, 155);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(190, 255, 155,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} ")
        self.pushButton_test_plot.setObjectName("pushButton_test_plot")'''
        self.pushButton_Analysis = QtWidgets.QPushButton(self.frame_body)
        (self.pushButton_Analysis).clicked.connect(self.model_training_plot)##############################
        self.pushButton_Analysis.setGeometry(QtCore.QRect(540, 410, 251, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_Analysis.setFont(font)
        self.pushButton_Analysis.setStyleSheet("QPushButton{ \n"
"    border:rgb(0, 255, 127);\n"
"    background-color:rgb(123, 255, 83);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(123, 255, 83,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} ")
        self.pushButton_Analysis.setObjectName("pushButton_Analysis")
        self.verticalLayout.addWidget(self.frame_body)
        self.frame_back = QtWidgets.QFrame(self.backgrd_frame)
        self.frame_back.setMinimumSize(QtCore.QSize(0, 78))
        self.frame_back.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_back.setObjectName("frame_back")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_back)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_back)
        (self.pushButton_back).clicked.connect(lambda:MainWindow.hide()) ####################################333333333//////////////////
        self.pushButton_back.setMinimumSize(QtCore.QSize(150, 29))
        self.pushButton_back.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.pushButton_back.setFont(font)
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
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_back)
        (self.pushButton_exit).clicked.connect(exit) ##############3
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(10)
        self.pushButton_exit.setFont(font)
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
        self.verticalLayout.addWidget(self.frame_back)
        self.dropshadow_layout_2.addWidget(self.backgrd_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.precision,self.recall,self.f_score,self.y_true,self.y_pred,self.prob=train_test_algo.give_metrics_parameter()#############

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Model Training and Testing"))
        self.label.setToolTip(_translate("MainWindow", "value of K for K Fold Algorithm"))
        self.label.setText(_translate("MainWindow", "Enter Value of K:"))
        self.plainTextEdit_k_value.setToolTip(_translate("MainWindow", "value of K for K Fold Algorithm"))
        self.plainTextEdit_k_value.setPlaceholderText(_translate("MainWindow", "Default: 5"))
        self.pushButton_hint.setText(_translate("MainWindow", "Hint"))
        self.pushButton_training.setText(_translate("MainWindow", "Model Training and Testing"))
        #self.pushButton_train_plot.setText(_translate("MainWindow", "View Mosaic Plot"))
        #self.pushButton_test_plot.setText(_translate("MainWindow", "View Confusion Matrix"))
        self.pushButton_Analysis.setText(_translate("MainWindow", "View Confusion Matrix"))
        self.pushButton_back.setText(_translate("MainWindow", "Back to Home Window"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit Application"))
        
        
    def K_hint(self):
        msg=QMessageBox()
        msg.setWindowTitle("Hint")
        text="""Cross-validation  has a single parameter called k that refers to the number of groups that a given data sample is to be split into.
        \nEnter interger value. eg. 5,10. \nTraining time is directly proportional to value of K."""
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        x=msg.exec_()
        
    def check_val_k(self,val):
        if(len(val)==0):
            return 2
            
        elif(val.isdigit()):
            return int(val)
            
        else:
            return "error"

    def plot_confusion_matrix(self,cm, classes ,normalize=True, title='Confusion matrix', cmap=plt.cm.Blues):
        """  This function prints and plots the confusion matrix.  Normalization can be applied by setting `normalize=True`."""
        #classes=['0','1','2']
        if normalize:
            cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=45)
        plt.yticks(tick_marks, classes)
        
        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")

        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('Predicted label')    
    
    
    def model_training_fxn(self):
        desc=self.plainTextEdit_k_value.toPlainText()
        checked_value = self.check_val_k(str(desc))
        if(checked_value=="error"):
            msg=QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid input, Please enter only interger value!")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()
            
        else:
            if checked_value>10:
                checked_value=2
                
            if checked_value<2:
                checked_value=2
                
            check_val=2
            
            val_check2=train_test_algo.training_testing_fxn(check_val)
                
            msg=QMessageBox()
            msg.setWindowTitle("Task Completed")
            msg.setText("Data has been trained and tested successfully")
            msg.setIcon(QMessageBox.Information)
            x=msg.exec_()
            self.data_trained_validation=1
            
            
    def model_training_plot(self,plot_select):
                
                classes = ['0','1','2']
                conf_matrix = confusion_matrix(self.y_true,self.y_pred)
                print("y_true: ",self.y_true)
                print("y_pred: ",self.y_pred)
                plt.figure()
                self.plot_confusion_matrix(conf_matrix,classes=classes,title='Confusion Matrix')
                plt.show()
        
        



'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''