# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QMovie,QBrush,QColor
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import pandas as pd
import numpy as np  
import os
import matplotlib.pyplot as plt
import re
import glob
import json
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import scikitplot 
import train_test_algo
from sklearn.metrics import confusion_matrix
from statsmodels.graphics import mosaicplot
from pandas_ml import ConfusionMatrix
import itertools
import pickle
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings("ignore")

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_model_eval(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 515)
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
        self.frame = QtWidgets.QFrame(self.backgrd_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 255))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(260, 40, 401, 113))
        self.tableWidget.setStyleSheet("background-color: rgb(85, 152, 203);")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(101, 200, 59))
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 127))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(2, 2, item)
        '''self.label_current = QtWidgets.QLabel(self.frame_2)
        self.label_current.setGeometry(QtCore.QRect(326, 170, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_current.setFont(font)
        self.label_current.setStyleSheet("color: rgb(255, 255, 0);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_current.setObjectName("label_current")'''
        self.label_current_2 = QtWidgets.QLabel(self.frame_2)
        self.label_current_2.setGeometry(QtCore.QRect(326, 190, 311, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_current_2.setFont(font)
        self.label_current_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_current_2.setObjectName("label_current_2")
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(9, 53))
        self.frame_3.setMaximumSize(QtCore.QSize(16777214, 54))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        (self.pushButton).clicked.connect(lambda:self.plot_graph_eval(1))######################################
        self.pushButton.setMinimumSize(QtCore.QSize(150, 29))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 25))
        self.pushButton.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color:rgb(166, 200, 101);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(166, 200, 101,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        (self.pushButton_2).clicked.connect(lambda:self.plot_graph_eval(2))######################################
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 29))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 25))
        self.pushButton_2.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color:rgb(166, 200, 101);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(166, 200, 101,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)
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
        self.show_accuracy(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Model Evaluation"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Class 0 (easy)"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Class 1 (medium)"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Class 2 (hard)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Precision"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Recall"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "F Score"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        
        self.xx=str(self.precision[0])
        item=self.tableWidget.setItem(0, 0,QTableWidgetItem(self.xx))
        
        self.xx=str(self.recall[0])
        self.tableWidget.setItem(0, 1,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.recall[0]"))
        
        self.xx=str(self.f_score[0])
        self.tableWidget.setItem(0, 2,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.f_score[0]"))
        
        self.xx=str(self.precision[1])
        self.tableWidget.setItem(1, 0,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.precision[1]"))
        
        
        self.xx=str(self.recall[1])
        self.tableWidget.setItem(1, 1,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.recall[1]"))
        
        self.xx=str(self.f_score[1])
        self.tableWidget.setItem(1, 2,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.f_score[1]"))
        
        self.xx=str(self.precision[2])
        self.tableWidget.setItem(2, 0,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.precision[2]"))
        
        self.xx=str(self.recall[2])
        self.tableWidget.setItem(2, 1,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.recall[2]"))
        
        self.xx=str(self.f_score[2])
        self.tableWidget.setItem(2, 2,QTableWidgetItem(self.xx))
        #item.setText(_translate("MainWindow", "self.f_score[2]"))
        
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        #self.label_current.setText(_translate("MainWindow", "Current Overall accuracy: "))
        self.label_current_2.setText(_translate("MainWindow", "Total Overall accuracy:    "))
        self.pushButton.setText(_translate("MainWindow", "View AUC/ROC curve "))
        self.pushButton_2.setText(_translate("MainWindow", "View Mosaic Plot"))
        self.pushButton_back.setText(_translate("MainWindow", "Back to Home Window"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit Application"))
        
        
    def plot_graph_eval(self,val_option):
        if(val_option==1):
            fpr = {}
            tpr = {}
            thresh ={}
            roc_auc = dict()
            n_class = 3

            for i in range(n_class):    
                fpr[i], tpr[i], thresh[i] = roc_curve(self.y_true,self.prob,pos_label=i)
                roc_auc[i] = auc(fpr[i], tpr[i])
                
            # plotting
            
            plt.plot(fpr[0], tpr[0], linestyle='--',color='orange', label='Class 0 vs Rest: (area = %0.2f)' % roc_auc[0])
            plt.plot(fpr[1], tpr[1], linestyle='--',color='green', label='Class 1 vs Rest: (area = %0.2f)' % roc_auc[1])
            plt.plot(fpr[2], tpr[2], linestyle='--',color='blue', label='Class 2 vs Rest: (area = %0.2f)' % roc_auc[2])
            plt.title('Multiclass ROC curve')
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive rate')
            plt.legend(loc='best')
            plt.show()
            
        else:
        
                with open('mosaic_results.pickle', 'rb') as f:
                    obj = pickle.load(f)
                mosaicplot.mosaic(data=obj, index=['True_Classes','Predicted_Classes'], title='Mosaic Plot')
                plt.show()
                
    def show_accuracy(self,MainWindow):
        cm = ConfusionMatrix(self.y_true, self.y_pred)
        
        sum_overall_accuracy = 0
        total_predictions = 0
        
        for num_pred in range(len(self.y_pred)):
            if(self.y_pred[num_pred] == self.y_true[num_pred]):
                sum_overall_accuracy += 1
            total_predictions += 1
            
        curr_acc= 'Current Overall accuracy:  '+str(cm.stats()['overall']['Accuracy'])
        total_acc='Total Overall Accuracy:   ' + str(sum_overall_accuracy/total_predictions)
            
        _translate = QtCore.QCoreApplication.translate
        #self.label_current.setText(_translate("MainWindow", curr_acc))
        self.label_current_2.setText(_translate("MainWindow", total_acc))
        
        '''
        print('Current Overall accuracy: ' + curr_acc)
        if total_predictions != 0:
            print('Total Overall Accuracy: ' + str(sum_overall_accuracy/total_predictions))
        else:
            print('Total Overall Accuracy: ' + str(cm.stats()['overall']['Accuracy']))
        '''
 
                
    


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