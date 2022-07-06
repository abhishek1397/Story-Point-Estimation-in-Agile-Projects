


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import *
#from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
from PyQt5.QtGui import QMovie
import model
import warnings
warnings.filterwarnings("ignore")


class Ui_MainWindow_calst(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 681)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_title = QtWidgets.QFrame(self.backgrd_frame)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 55))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.frame_title.setFont(font)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.verticalLayout_4.addWidget(self.label_title)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_content = QtWidgets.QFrame(self.backgrd_frame)
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_content)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_oneSP = QtWidgets.QFrame(self.frame_content)
        self.frame_oneSP.setMinimumSize(QtCore.QSize(750, 0))
        self.frame_oneSP.setMaximumSize(QtCore.QSize(750, 16777215))
        self.frame_oneSP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_oneSP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_oneSP.setObjectName("frame_oneSP")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_oneSP)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.frame_oneSP)
        self.frame.setMinimumSize(QtCore.QSize(0, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_one_head = QtWidgets.QFrame(self.frame_oneSP)
        self.frame_one_head.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_one_head.setMaximumSize(QtCore.QSize(16777215, 130))
        self.frame_one_head.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_one_head.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_one_head.setObjectName("frame_one_head")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_one_head)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_one_head)
        self.label.setMinimumSize(QtCore.QSize(300, 80))
        self.label.setMaximumSize(QtCore.QSize(300, 80))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 0);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_5.addWidget(self.frame_one_head)
        self.frame_one_title = QtWidgets.QFrame(self.frame_oneSP)
        self.frame_one_title.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_one_title.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_one_title.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame_one_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_one_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_one_title.setObjectName("frame_one_title")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_one_title)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_one_title)
        
        self.textEdit_3.setMinimumSize(QtCore.QSize(400, 60))
        self.textEdit_3.setMaximumSize(QtCore.QSize(400, 60))
        self.textEdit_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.textEdit_3.setAcceptRichText(False)  #################################
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setStyleSheet("QTextEdit{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color:rgb(255, 170, 255);\n"
"}\n"
" \n"
"")
        self.textEdit_3.setUndoRedoEnabled(True) ########################333
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_5.addWidget(self.textEdit_3)
        self.verticalLayout_5.addWidget(self.frame_one_title)
        self.frame_one_desc = QtWidgets.QFrame(self.frame_oneSP)
        self.frame_one_desc.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_one_desc.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_one_desc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_one_desc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_one_desc.setObjectName("frame_one_desc")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_one_desc)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_one_desc)
        self.textEdit_2.setMinimumSize(QtCore.QSize(400, 60))
        self.textEdit_2.setMaximumSize(QtCore.QSize(400, 60))
        self.textEdit_2.setAcceptRichText(False) #######################3
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QTextEdit{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color:rgb(255, 170, 255);\n"
"}\n"
" \n"
"")
        self.textEdit_2.setUndoRedoEnabled(True)   ###########################33
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_6.addWidget(self.textEdit_2)
        self.verticalLayout_5.addWidget(self.frame_one_desc)
        self.frame_one_output = QtWidgets.QFrame(self.frame_oneSP)
        self.frame_one_output.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_one_output.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_one_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_one_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_one_output.setObjectName("frame_one_output")
        self.label_2 = QtWidgets.QLabel(self.frame_one_output)
        self.label_2.setGeometry(QtCore.QRect(9, 9, 550, 50))
        self.label_2.setMinimumSize(QtCore.QSize(550, 50))
        self.label_2.setMaximumSize(QtCore.QSize(550, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.frame_one_output)
        self.horizontalLayout_2.addWidget(self.frame_oneSP)
        self.frame_partition = QtWidgets.QFrame(self.frame_content)
        self.frame_partition.setMinimumSize(QtCore.QSize(65, 0))
        self.frame_partition.setMaximumSize(QtCore.QSize(67, 16777215))
        self.frame_partition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_partition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_partition.setObjectName("frame_partition")
        self.horizontalLayout_2.addWidget(self.frame_partition)
        self.frame_multiSP = QtWidgets.QFrame(self.frame_content)
        self.frame_multiSP.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_multiSP.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_multiSP.setObjectName("frame_multiSP")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_multiSP)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_label_title = QtWidgets.QFrame(self.frame_multiSP)
        self.frame_label_title.setMinimumSize(QtCore.QSize(0, 109))
        self.frame_label_title.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_label_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_title.setObjectName("frame_label_title")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_label_title)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_multiSP = QtWidgets.QLabel(self.frame_label_title)
        self.label_multiSP.setMinimumSize(QtCore.QSize(0, 50))
        self.label_multiSP.setMaximumSize(QtCore.QSize(304, 79))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_multiSP.setFont(font)
        self.label_multiSP.setStyleSheet("color: rgb(255, 255, 0);\n"
"border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.label_multiSP.setAlignment(QtCore.Qt.AlignCenter)
        self.label_multiSP.setWordWrap(True)
        self.label_multiSP.setObjectName("label_multiSP")
        self.verticalLayout_8.addWidget(self.label_multiSP)
        self.verticalLayout.addWidget(self.frame_label_title)
        self.frame_import_csv = QtWidgets.QFrame(self.frame_multiSP)
        self.frame_import_csv.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_import_csv.setMaximumSize(QtCore.QSize(16777215, 89))
        self.frame_import_csv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_import_csv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_import_csv.setObjectName("frame_import_csv")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_import_csv)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_import_csv = QtWidgets.QPushButton(self.frame_import_csv)
        self.fname=""##########################
        (self.pushButton_import_csv).clicked.connect(self.import_file) ####################################333
        self.pushButton_import_csv.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton_import_csv.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_import_csv.setFont(font)
        self.pushButton_import_csv.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(85, 255, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_import_csv.setObjectName("pushButton_import_csv")
        self.verticalLayout_6.addWidget(self.pushButton_import_csv)
        self.verticalLayout.addWidget(self.frame_import_csv)
        self.frame_import_csv_2 = QtWidgets.QFrame(self.frame_multiSP)
        self.frame_import_csv_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_import_csv_2.setMaximumSize(QtCore.QSize(16777215, 113))
        self.frame_import_csv_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_import_csv_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_import_csv_2.setObjectName("frame_import_csv_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_import_csv_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_import_advice = QtWidgets.QPushButton(self.frame_import_csv_2)
        self.button_advice="sheet_sample.png"############################################
        (self.pushButton_import_advice).clicked.connect(lambda:os.system(self.button_advice)) ####################3333
        self.pushButton_import_advice.setMinimumSize(QtCore.QSize(150, 36))
        self.pushButton_import_advice.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()  
        font.setPointSize(10)
        self.pushButton_import_advice.setFont(font)
        self.pushButton_import_advice.setToolTipDuration(0)
        self.pushButton_import_advice.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 255, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(85, 255, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_import_advice.setObjectName("pushButton_import_advice")
        self.verticalLayout_7.addWidget(self.pushButton_import_advice)
        self.frame_ideal = QtWidgets.QFrame(self.frame_import_csv_2)
        self.frame_ideal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ideal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ideal.setObjectName("frame_ideal")
        self.verticalLayout_7.addWidget(self.frame_ideal)
        self.verticalLayout.addWidget(self.frame_import_csv_2)
        self.horizontalLayout_2.addWidget(self.frame_multiSP)
        self.verticalLayout_2.addWidget(self.frame_content)
        self.frame_calSP_btns = QtWidgets.QFrame(self.backgrd_frame)
        self.frame_calSP_btns.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_calSP_btns.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_calSP_btns.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_calSP_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_calSP_btns.setObjectName("frame_calSP_btns")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_calSP_btns)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_6 = QtWidgets.QFrame(self.frame_calSP_btns)
        self.frame_6.setMinimumSize(QtCore.QSize(750, 60))
        self.frame_6.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_predictSP = QtWidgets.QPushButton(self.frame_6)
        (self.pushButton_predictSP).clicked.connect(lambda:self.cal_single_sp(MainWindow)) ##############3########################33
        self.pushButton_predictSP.setMinimumSize(QtCore.QSize(300, 40))
        self.pushButton_predictSP.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_predictSP.setFont(font)
        self.pushButton_predictSP.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(85, 255, 255,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_predictSP.setObjectName("pushButton_predictSP")
        self.horizontalLayout_3.addWidget(self.pushButton_predictSP)
        self.horizontalLayout_7.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_calSP_btns)
        self.frame_4.setMinimumSize(QtCore.QSize(514, 60))
        self.frame_4.setMaximumSize(QtCore.QSize(461, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_2 = QtWidgets.QFrame(self.frame_4)
        self.frame_2.setMinimumSize(QtCore.QSize(33, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(16, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_8.addWidget(self.frame_2)
        self.pushButton_exportSP = QtWidgets.QPushButton(self.frame_4)
        (self.pushButton_exportSP).clicked.connect(self.cal_multiple_sp) ####################################333333333//////////////////
        self.pushButton_exportSP.setMinimumSize(QtCore.QSize(300, 30))
        self.pushButton_exportSP.setMaximumSize(QtCore.QSize(300, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_exportSP.setFont(font)
        self.pushButton_exportSP.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(85, 255, 255,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_exportSP.setObjectName("pushButton_exportSP")
        self.horizontalLayout_8.addWidget(self.pushButton_exportSP)
        self.frame_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_3.setMaximumSize(QtCore.QSize(130, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_8.addWidget(self.frame_3)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.verticalLayout_2.addWidget(self.frame_calSP_btns)
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
        self.verticalLayout_2.addWidget(self.frame_back)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.dropshadow_layout_2.addWidget(self.backgrd_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Story Point Estimation Tool"))
        self.label.setText(_translate("MainWindow", "Predicting Single Story  Point"))
        self.textEdit_3.setPlaceholderText(_translate("MainWindow", "Issue Title"))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Issue Description"))
        self.label_2.setText(_translate("MainWindow", "The Story Point is: "))
        self.label_multiSP.setText(_translate("MainWindow", "Predicting Multiple Story Points"))
        self.pushButton_import_csv.setText(_translate("MainWindow", "Import Csv"))
        self.pushButton_import_advice.setToolTip(_translate("MainWindow", "csv should be in given format only"))
        self.pushButton_import_advice.setText(_translate("MainWindow", "csv format"))
        self.pushButton_predictSP.setText(_translate("MainWindow", "Predict SP"))
        self.pushButton_exportSP.setText(_translate("MainWindow", "Predict SP and Export csv"))
        self.pushButton_back.setText(_translate("MainWindow", "Back to Home Window"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit Application"))
        
        

    def import_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fname=""
        self.fname,_=QFileDialog.getOpenFileName(self,'Open file','c:\\','CSV files (*.csv)')
        print("File name is: ")
        print(self.fname)
        
        
    def show_popup(self,i):
        msg=QMessageBox()
        #msg.setWindowTitle("Error")
        
        if(i==1):
            msg.setWindowTitle("Error")
            msg.setText("Please enter both Title and Description!")
            msg.setIcon(QMessageBox.Warning)
        elif(i==2):
            msg.setWindowTitle("Error")
            msg.setText("CSV in wrong format")    
            msg.setIcon(QMessageBox.Warning)
        elif(i==3):
            msg.setWindowTitle("Task Completed")
            msg.setText("The Story Points have been saved to selected file")    
            msg.setIcon(QMessageBox.Information)
        elif(i==4):
            msg.setWindowTitle("Error")
            msg.setText("No CSV selected")    
            msg.setIcon(QMessageBox.Warning)
            
        else:
            msg.setWindowTitle("Error")
            msg.setText("Please select file!")
            msg.setIcon(QMessageBox.Warning)
        
        x=msg.exec_()
    
    def cal_single_sp(self,MainWindow):
        title=self.textEdit_3.toPlainText()
        desc=self.textEdit_2.toPlainText()
        
        if((len(title) == 0) or len(desc) == 0):
            self.show_popup(i=1)
        else:
            _translate = QtCore.QCoreApplication.translate
            predicted_sp = model.calsp(title,desc)
            stri="The Story Point is: "+str(predicted_sp)
            self.label_2.setText(_translate("MainWindow", stri))
            print("value present")

    def cal_multiple_sp(self,MainWindow):
        if((len(self.fname) == 0)):
            self.show_popup(i=4)
            
        else:
            return_val=model.calsp_csv(self.fname)
            if(return_val==0):
                self.show_popup(i=2)
            else:
                self.show_popup(i=3)
                
            
    
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_calst()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''
