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
import hashlib
from ui_main_calst_user import Ui_MainWindow_calsp_user
from ui_main import Ui_MainWindow
import warnings
warnings.filterwarnings("ignore")


class Ui_MainWindow_login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 653, 473))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.147727 rgba(11, 131, 120, 219), stop:0.5209 rgba(28, 29, 73, 255));\n"
"    \n"
"    color: rgba(255, 255, 255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"    background-position:calc(100% - 10px) center;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.147727 rgba(150,123,111,219), stop:0.5209 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(341, 46, 271, 379))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 331, 411))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 98, 112, 255), stop:1 rgba(255, 107, 107, 255));\n"
"border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(380, 90, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgba(0,0,0,200);")
        self.label_3.setObjectName("label_3")
        self.user_name = QtWidgets.QLineEdit(self.widget)
        self.user_name.setGeometry(QtCore.QRect(380, 170, 195, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(380, 235, 195, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom:7px;\n"
"")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.login_button = QtWidgets.QPushButton(self.widget)
        (self.login_button).clicked.connect(self.login_details) ####################################333333333//////////////////
        self.login_button.setGeometry(QtCore.QRect(380, 327, 195, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login_button.setFont(font)
        self.login_button.setStyleSheet("QPushButton{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    \n"
"    color: rgba(255, 255, 255,210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150,123,111,255);\n"
"    background-position:calc(100% - 10px) center;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"")
        self.login_button.setObjectName("login_button")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(46, 59, 231, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(37)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Log In"))
        self.user_name.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.password.setPlaceholderText(_translate("MainWindow", "  Password"))
        self.login_button.setText(_translate("MainWindow", "L o g  I n"))
        self.label_4.setText(_translate("MainWindow", "Story Point \n"
"Estimation\n"
"Tool"))

    def login_details(self):
        
        usname=self.user_name.text()
        passw1=self.password.text()
        
        if(len(passw1)==0 or len(usname)==0):
            msg=QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Please Enter username and password")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()
                
        elif(usname=="admin" and passw1=="admin"):
            print("hello admin")
            
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
            
        elif(usname=="user" and passw1=="user"): 
            print("hello user")
            
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow_calsp_user()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
            
        else:
            msg=QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setText("Incorrect username or password")
            msg.setIcon(QMessageBox.Warning)
            x=msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
