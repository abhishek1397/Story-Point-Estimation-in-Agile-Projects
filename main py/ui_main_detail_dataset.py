# -*- coding: utf-8 -*-



import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import webbrowser
import warnings
warnings.filterwarnings("ignore")

class Ui_MainWindow_dataset_details(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 1000)
        MainWindow.showMaximized() #############
        MainWindow.setMinimumSize(QtCore.QSize(1000, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.dropshadow_layout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.dropshadow_layout_2.setContentsMargins(10, 10, 10, 10)
        self.dropshadow_layout_2.setSpacing(0)
        self.dropshadow_layout_2.setObjectName("dropshadow_layout_2")
        self.backgrd_frame = QtWidgets.QFrame(self.centralwidget)
        self.backgrd_frame.setEnabled(True)
        self.backgrd_frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(28, 29, 73, 255), stop:0.486425 rgba(28, 29, 73, 255));\n"
"border-radius: 10px;\n"
"")
        self.backgrd_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.backgrd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgrd_frame.setObjectName("backgrd_frame")
        self.backgrd_frame_2 = QtWidgets.QFrame(self.backgrd_frame)
        self.backgrd_frame_2.setGeometry(QtCore.QRect(9, 9, 1366, 660))
        self.backgrd_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backgrd_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backgrd_frame_2.setObjectName("backgrd_frame_2")
        self.frame_title = QtWidgets.QFrame(self.backgrd_frame_2)
        self.frame_title.setGeometry(QtCore.QRect(9, 10, 1275, 30))
        self.frame_title.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 28))
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_title = QtWidgets.QLabel(self.frame_title)
        self.label_title.setMinimumSize(QtCore.QSize(0, 21))
        self.label_title.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color:rgb(255, 255, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_2.addWidget(self.label_title)
        self.frame_body = QtWidgets.QFrame(self.backgrd_frame_2)
        self.frame_body.setGeometry(QtCore.QRect(10, 43, 1275, 620))
        self.frame_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_body.setObjectName("frame_body")
        self.frame_content = QtWidgets.QFrame(self.frame_body)
        self.frame_content.setGeometry(QtCore.QRect(9, 5, 1257, 638))
        self.frame_content.setMinimumSize(QtCore.QSize(0, 638))
        self.frame_content.setMaximumSize(QtCore.QSize(16777215, 625))
        self.frame_content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.frame = QtWidgets.QFrame(self.frame_content)
        self.frame.setGeometry(QtCore.QRect(15, -9, 937, 620))
        self.frame.setMinimumSize(QtCore.QSize(923, 561))
        self.frame.setMaximumSize(QtCore.QSize(937, 622))
        self.frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(3, 10, 938, 495))
        self.tableWidget.setMinimumSize(QtCore.QSize(938, 495))
        self.tableWidget.setMaximumSize(QtCore.QSize(491, 450))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(85, 152, 203);")
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(17)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(6, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(10, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(11, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(12, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(13, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(14, 10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(15, 10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(16, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setItem(16, 2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(83)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(43)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.frame_view_dataset = QtWidgets.QFrame(self.frame_content)
        self.frame_view_dataset.setGeometry(QtCore.QRect(961, -6, 80, 620))
        self.frame_view_dataset.setMinimumSize(QtCore.QSize(80, 0))
        self.frame_view_dataset.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_view_dataset.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_view_dataset.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_view_dataset.setObjectName("frame_view_dataset")
        self.label_dataset_view = QtWidgets.QLabel(self.frame_view_dataset)
        self.label_dataset_view.setGeometry(QtCore.QRect(0, 6, 77, 28))
        self.label_dataset_view.setMinimumSize(QtCore.QSize(77, 28))
        self.label_dataset_view.setMaximumSize(QtCore.QSize(73, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_dataset_view.setFont(font)
        self.label_dataset_view.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_dataset_view.setAutoFillBackground(False)
        self.label_dataset_view.setStyleSheet("QLabel{ \n"
"    border:5px sold rgb(85, 0, 127);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label_dataset_view.setTextFormat(QtCore.Qt.AutoText)
        self.label_dataset_view.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dataset_view.setWordWrap(True)
        self.label_dataset_view.setOpenExternalLinks(False)
        self.label_dataset_view.setObjectName("label_dataset_view")
        self.dataset_view_1_mesos = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli1="datasets\\mesos.csv"
        (self.dataset_view_1_mesos).clicked.connect(lambda:os.system(self.appli1)) ##############3########################33
        self.dataset_view_1_mesos.setGeometry(QtCore.QRect(2, 37, 73, 21))
        self.dataset_view_1_mesos.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_1_mesos.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_1_mesos.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_1_mesos.setObjectName("dataset_view_1_mesos")
        self.dataset_view_2_usergrid = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli2="datasets\\usergrid.csv"
        (self.dataset_view_2_usergrid).clicked.connect(lambda:os.system(self.appli2)) ##############3########################33
        self.dataset_view_2_usergrid.setGeometry(QtCore.QRect(2, 64, 73, 21))
        self.dataset_view_2_usergrid.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_2_usergrid.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_2_usergrid.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_2_usergrid.setObjectName("dataset_view_2_usergrid")
        self.dataset_view_3_appcelerator = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli3="datasets\\appceleratorstudio.csv"
        (self.dataset_view_3_appcelerator).clicked.connect(lambda:os.system(self.appli3)) ##############3########################33
        self.dataset_view_3_appcelerator.setGeometry(QtCore.QRect(2, 91, 73, 21))
        self.dataset_view_3_appcelerator.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_3_appcelerator.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_3_appcelerator.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_3_appcelerator.setObjectName("dataset_view_3_appcelerator")
        self.dataset_view_4_aptana = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli4="datasets\\aptanastudio.csv"
        (self.dataset_view_4_aptana).clicked.connect(lambda:os.system(self.appli4)) ##############3########################33
        self.dataset_view_4_aptana.setGeometry(QtCore.QRect(2, 120, 73, 21))
        self.dataset_view_4_aptana.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_4_aptana.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_4_aptana.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_4_aptana.setObjectName("dataset_view_4_aptana")
        self.dataset_view_5_titanium = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli5="datasets\\titanium.csv"
        (self.dataset_view_5_titanium).clicked.connect(lambda:os.system(self.appli5)) ##############3########################33
        self.dataset_view_5_titanium.setGeometry(QtCore.QRect(2, 148, 73, 21))
        self.dataset_view_5_titanium.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_5_titanium.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_5_titanium.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_5_titanium.setObjectName("dataset_view_5_titanium")
        self.dataset_view_6_duracloud = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli6="datasets\\duracloud.csv"
        (self.dataset_view_6_duracloud).clicked.connect(lambda:os.system(self.appli6)) ##############3########################33
        self.dataset_view_6_duracloud.setGeometry(QtCore.QRect(2, 174, 73, 21))
        self.dataset_view_6_duracloud.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_6_duracloud.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_6_duracloud.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_6_duracloud.setObjectName("dataset_view_6_duracloud")
        self.dataset_view_12_mule = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli12="datasets\\mule.csv"
        (self.dataset_view_12_mule).clicked.connect(lambda:os.system(self.appli12)) ##############3########################33
        self.dataset_view_12_mule.setGeometry(QtCore.QRect(2, 345, 73, 21))
        self.dataset_view_12_mule.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_12_mule.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_12_mule.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_12_mule.setObjectName("dataset_view_12_mule")
        self.dataset_view_11_data = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli11="datasets\\datamanagement.csv"
        (self.dataset_view_11_data).clicked.connect(lambda:os.system(self.appli11)) ##############3########################33
        self.dataset_view_11_data.setGeometry(QtCore.QRect(2, 317, 73, 21))
        self.dataset_view_11_data.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_11_data.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_11_data.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_11_data.setObjectName("dataset_view_11_data")
        self.dataset_view_10_moodle = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli10="datasets\\moodle.csv"
        (self.dataset_view_10_moodle).clicked.connect(lambda:os.system(self.appli10)) ##############3########################33
        self.dataset_view_10_moodle.setGeometry(QtCore.QRect(2, 288, 73, 21))
        self.dataset_view_10_moodle.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_10_moodle.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_10_moodle.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_10_moodle.setObjectName("dataset_view_10_moodle")
        self.dataset_view_9_jira = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli9="datasets\\jirasoftware.csv"
        (self.dataset_view_9_jira).clicked.connect(lambda:os.system(self.appli9)) ##############3########################33
        self.dataset_view_9_jira.setGeometry(QtCore.QRect(2, 260, 73, 21))
        self.dataset_view_9_jira.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_9_jira.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_9_jira.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_9_jira.setObjectName("dataset_view_9_jira")
        self.dataset_view_8_clover = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli8="datasets\\clover.csv"
        (self.dataset_view_8_clover).clicked.connect(lambda:os.system(self.appli8)) ##############3########################33
        self.dataset_view_8_clover.setGeometry(QtCore.QRect(2, 230, 73, 21))
        self.dataset_view_8_clover.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_8_clover.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_8_clover.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_8_clover.setObjectName("dataset_view_8_clover")
        self.dataset_view_7_bamboo = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli7="datasets\\bamboo.csv"
        (self.dataset_view_7_bamboo).clicked.connect(lambda:os.system(self.appli7)) ##############3########################33
        self.dataset_view_7_bamboo.setGeometry(QtCore.QRect(2, 202, 73, 21))
        self.dataset_view_7_bamboo.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_7_bamboo.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_7_bamboo.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_7_bamboo.setObjectName("dataset_view_7_bamboo")
        self.dataset_view_16_talendesb = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli16="datasets\\talendesb.csv"
        (self.dataset_view_16_talendesb).clicked.connect(lambda:os.system(self.appli16)) ##############3########################33
        self.dataset_view_16_talendesb.setGeometry(QtCore.QRect(2, 458, 73, 21))
        self.dataset_view_16_talendesb.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_16_talendesb.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_16_talendesb.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_16_talendesb.setObjectName("dataset_view_16_talendesb")
        self.dataset_view_15_talenddata = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli15="datasets\\talenddataquality.csv"
        (self.dataset_view_15_talenddata).clicked.connect(lambda:os.system(self.appli15)) ##############3########################33
        self.dataset_view_15_talenddata.setGeometry(QtCore.QRect(2, 429, 73, 21))
        self.dataset_view_15_talenddata.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_15_talenddata.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_15_talenddata.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_15_talenddata.setObjectName("dataset_view_15_talenddata")
        self.dataset_view_14_spring = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli14="datasets\\springxd.csv"
        (self.dataset_view_14_spring).clicked.connect(lambda:os.system(self.appli14)) ##############3########################33
        self.dataset_view_14_spring.setGeometry(QtCore.QRect(2, 399, 73, 21))
        self.dataset_view_14_spring.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_14_spring.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_14_spring.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_14_spring.setObjectName("dataset_view_14_spring")
        self.dataset_view_13_mulestudio = QtWidgets.QPushButton(self.frame_view_dataset)
        self.appli13="datasets\\mulestudio.csv"
        (self.dataset_view_13_mulestudio).clicked.connect(lambda:os.system(self.appli13)) ##############3########################33
        self.dataset_view_13_mulestudio.setGeometry(QtCore.QRect(2, 372, 73, 21))
        self.dataset_view_13_mulestudio.setMinimumSize(QtCore.QSize(73, 18))
        self.dataset_view_13_mulestudio.setMaximumSize(QtCore.QSize(73, 21))
        self.dataset_view_13_mulestudio.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.dataset_view_13_mulestudio.setObjectName("dataset_view_13_mulestudio")
        self.frame_before_preprocess = QtWidgets.QFrame(self.frame_content)
        self.frame_before_preprocess.setGeometry(QtCore.QRect(1054, -6, 93, 620))
        self.frame_before_preprocess.setMinimumSize(QtCore.QSize(91, 0))
        self.frame_before_preprocess.setMaximumSize(QtCore.QSize(93, 16777215))
        self.frame_before_preprocess.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_before_preprocess.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_before_preprocess.setObjectName("frame_before_preprocess")
        self.label_2 = QtWidgets.QLabel(self.frame_before_preprocess)
        self.label_2.setGeometry(QtCore.QRect(0, 6, 90, 28))
        self.label_2.setMinimumSize(QtCore.QSize(90, 28))
        self.label_2.setMaximumSize(QtCore.QSize(26, 26))
        self.label_2.setStyleSheet("QLabel{ \n"
"    border:5px sold rgb(85, 0, 127);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.vis_before_1_mesos = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before1="datasets\\Before_preprocessing\\mesos.png"
        (self.vis_before_1_mesos).clicked.connect(lambda:os.system(self.before1)) ##############3########################33
        self.vis_before_1_mesos.setGeometry(QtCore.QRect(7, 37, 73, 21))
        self.vis_before_1_mesos.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_1_mesos.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_1_mesos.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_1_mesos.setObjectName("vis_before_1_mesos")
        self.vis_before_2_usergrid = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before2="datasets\\Before_preprocessing\\usergrid.png"
        (self.vis_before_2_usergrid).clicked.connect(lambda:os.system(self.before2)) ##############3########################33
        self.vis_before_2_usergrid.setGeometry(QtCore.QRect(7, 64, 73, 21))
        self.vis_before_2_usergrid.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_2_usergrid.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_2_usergrid.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_2_usergrid.setObjectName("vis_before_2_usergrid")
        self.vis_before_3_appcelerator = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before3="datasets\\Before_preprocessing\\appceleratorstudio.png"
        (self.vis_before_3_appcelerator).clicked.connect(lambda:os.system(self.before3)) ##############3########################33
        self.vis_before_3_appcelerator.setGeometry(QtCore.QRect(7, 91, 73, 21))
        self.vis_before_3_appcelerator.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_3_appcelerator.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_3_appcelerator.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_3_appcelerator.setObjectName("vis_before_3_appcelerator")
        self.vis_before_4_aptana = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before4="datasets\\Before_preprocessing\\aptanastudio.png"
        (self.vis_before_4_aptana).clicked.connect(lambda:os.system(self.before4)) ##############3########################33
        self.vis_before_4_aptana.setGeometry(QtCore.QRect(7, 120, 73, 21))
        self.vis_before_4_aptana.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_4_aptana.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_4_aptana.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_4_aptana.setObjectName("vis_before_4_aptana")
        self.vis_before_5_titanium = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before5="datasets\\Before_preprocessing\\titanium.png"
        (self.vis_before_5_titanium).clicked.connect(lambda:os.system(self.before5)) ##############3########################33
        self.vis_before_5_titanium.setGeometry(QtCore.QRect(7, 148, 73, 21))
        self.vis_before_5_titanium.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_5_titanium.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_5_titanium.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_5_titanium.setObjectName("vis_before_5_titanium")
        self.vis_before_6_duracloud = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before6="datasets\\Before_preprocessing\\duracloud.png"
        (self.vis_before_6_duracloud).clicked.connect(lambda:os.system(self.before6)) ##############3########################33
        self.vis_before_6_duracloud.setGeometry(QtCore.QRect(7, 174, 73, 21))
        self.vis_before_6_duracloud.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_6_duracloud.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_6_duracloud.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_6_duracloud.setObjectName("vis_before_6_duracloud")
        self.vis_before_7_bamboo = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before7="datasets\\Before_preprocessing\\bamboo.png"
        (self.vis_before_7_bamboo).clicked.connect(lambda:os.system(self.before7)) ##############3########################33
        self.vis_before_7_bamboo.setGeometry(QtCore.QRect(7, 202, 73, 21))
        self.vis_before_7_bamboo.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_7_bamboo.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_7_bamboo.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_7_bamboo.setObjectName("vis_before_7_bamboo")
        self.vis_before_8_clover = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before8="datasets\\Before_preprocessing\\clover.png"
        (self.vis_before_8_clover).clicked.connect(lambda:os.system(self.before8)) ##############3########################33
        self.vis_before_8_clover.setGeometry(QtCore.QRect(7, 230, 73, 21))
        self.vis_before_8_clover.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_8_clover.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_8_clover.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_8_clover.setObjectName("vis_before_8_clover")
        self.vis_before_9_jira = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before9="datasets\\Before_preprocessing\\jirasoftware.png"
        (self.vis_before_9_jira).clicked.connect(lambda:os.system(self.before9)) ##############3########################33
        self.vis_before_9_jira.setGeometry(QtCore.QRect(7, 260, 73, 21))
        self.vis_before_9_jira.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_9_jira.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_9_jira.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_9_jira.setObjectName("vis_before_9_jira")
        self.vis_before_10_moodle = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before10="datasets\\Before_preprocessing\\moodle.png"
        (self.vis_before_10_moodle).clicked.connect(lambda:os.system(self.before10)) ##############3########################33
        self.vis_before_10_moodle.setGeometry(QtCore.QRect(7, 288, 73, 21))
        self.vis_before_10_moodle.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_10_moodle.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_10_moodle.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_10_moodle.setObjectName("vis_before_10_moodle")
        self.vis_before_16_talendesb = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before16="datasets\\Before_preprocessing\\talendesb.png"
        (self.vis_before_16_talendesb).clicked.connect(lambda:os.system(self.before16)) ##############3########################33
        self.vis_before_16_talendesb.setGeometry(QtCore.QRect(7, 458, 73, 21))
        self.vis_before_16_talendesb.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_16_talendesb.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_16_talendesb.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_16_talendesb.setObjectName("vis_before_16_talendesb")
        self.vis_before_15_talenddata = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before15="datasets\\Before_preprocessing\\talenddataquality.png"
        (self.vis_before_15_talenddata).clicked.connect(lambda:os.system(self.before15)) ##############3########################33
        self.vis_before_15_talenddata.setGeometry(QtCore.QRect(7, 429, 73, 21))
        self.vis_before_15_talenddata.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_15_talenddata.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_15_talenddata.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_15_talenddata.setObjectName("vis_before_15_talenddata")
        self.vis_before_14_spring = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before14="datasets\\Before_preprocessing\\springxd.png"
        (self.vis_before_14_spring).clicked.connect(lambda:os.system(self.before14)) ##############3########################33
        self.vis_before_14_spring.setGeometry(QtCore.QRect(7, 399, 73, 21))
        self.vis_before_14_spring.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_14_spring.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_14_spring.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_14_spring.setObjectName("vis_before_14_spring")
        self.vis_before_13_mulestudio = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before13="datasets\\Before_preprocessing\\mulestudio.png"
        (self.vis_before_13_mulestudio).clicked.connect(lambda:os.system(self.before13)) ##############3########################33
        self.vis_before_13_mulestudio.setGeometry(QtCore.QRect(7, 372, 73, 21))
        self.vis_before_13_mulestudio.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_13_mulestudio.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_13_mulestudio.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_13_mulestudio.setObjectName("vis_before_13_mulestudio")
        self.vis_before_12_mule = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before12="datasets\\Before_preprocessing\\mule.png"
        (self.vis_before_12_mule).clicked.connect(lambda:os.system(self.before12)) ##############3########################33
        self.vis_before_12_mule.setGeometry(QtCore.QRect(7, 345, 73, 21))
        self.vis_before_12_mule.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_12_mule.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_12_mule.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_12_mule.setObjectName("vis_before_12_mule")
        self.vis_before_11_data = QtWidgets.QPushButton(self.frame_before_preprocess)
        self.before11="datasets\\Before_preprocessing\\datamanagement.png"
        (self.vis_before_11_data).clicked.connect(lambda:os.system(self.before11)) ##############3########################33
        self.vis_before_11_data.setGeometry(QtCore.QRect(7, 317, 73, 21))
        self.vis_before_11_data.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_before_11_data.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_before_11_data.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_before_11_data.setObjectName("vis_before_11_data")
        self.frame_after_preprocess = QtWidgets.QFrame(self.frame_content)
        self.frame_after_preprocess.setGeometry(QtCore.QRect(1155, -6, 91, 620))
        self.frame_after_preprocess.setMinimumSize(QtCore.QSize(91, 0))
        self.frame_after_preprocess.setMaximumSize(QtCore.QSize(30, 16777215))
        self.frame_after_preprocess.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_after_preprocess.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_after_preprocess.setObjectName("frame_after_preprocess")
        self.label_3 = QtWidgets.QLabel(self.frame_after_preprocess)
        self.label_3.setGeometry(QtCore.QRect(0, 6, 90, 28))
        self.label_3.setMinimumSize(QtCore.QSize(90, 28))
        self.label_3.setMaximumSize(QtCore.QSize(26, 26))
        self.label_3.setStyleSheet("QLabel{ \n"
"    border:5px sold rgb(85, 0, 127);\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.vis_after_1_mesos = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after1="datasets\\After_preprocessing\\mesos.png"
        (self.vis_after_1_mesos).clicked.connect(lambda:os.system(self.after1)) ##############3########################33
        self.vis_after_1_mesos.setGeometry(QtCore.QRect(7, 37, 73, 21))
        self.vis_after_1_mesos.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_1_mesos.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_1_mesos.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_1_mesos.setObjectName("vis_after_1_mesos")
        self.vis_after_10_moodle = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after10="datasets\\After_preprocessing\\moodle.png"
        (self.vis_after_10_moodle).clicked.connect(lambda:os.system(self.after10)) ##############3########################33
        self.vis_after_10_moodle.setGeometry(QtCore.QRect(7, 288, 73, 21))
        self.vis_after_10_moodle.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_10_moodle.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_10_moodle.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_10_moodle.setObjectName("vis_after_10_moodle")
        self.vis_after_9_jira = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after9="datasets\\After_preprocessing\\jirasoftware.png"
        (self.vis_after_9_jira).clicked.connect(lambda:os.system(self.after9)) ##############3########################33
        self.vis_after_9_jira.setGeometry(QtCore.QRect(7, 260, 73, 21))
        self.vis_after_9_jira.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_9_jira.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_9_jira.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_9_jira.setObjectName("vis_after_9_jira")
        self.vis_after_8_clover = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after8="datasets\\After_preprocessing\\clover.png"
        (self.vis_after_8_clover).clicked.connect(lambda:os.system(self.after8)) ##############3########################33
        self.vis_after_8_clover.setGeometry(QtCore.QRect(7, 230, 73, 21))
        self.vis_after_8_clover.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_8_clover.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_8_clover.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_8_clover.setObjectName("vis_after_8_clover")
        self.vis_after_7_bamboo = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after7="datasets\\After_preprocessing\\bamboo.png"
        (self.vis_after_7_bamboo).clicked.connect(lambda:os.system(self.after7)) ##############3########################33
        self.vis_after_7_bamboo.setGeometry(QtCore.QRect(7, 202, 73, 21))
        self.vis_after_7_bamboo.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_7_bamboo.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_7_bamboo.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_7_bamboo.setObjectName("vis_after_7_bamboo")
        self.vis_after_6_duracloud = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after6="datasets\\After_preprocessing\\duracloud.png"
        (self.vis_after_6_duracloud).clicked.connect(lambda:os.system(self.after6)) ##############3########################33
        self.vis_after_6_duracloud.setGeometry(QtCore.QRect(7, 174, 73, 21))
        self.vis_after_6_duracloud.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_6_duracloud.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_6_duracloud.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_6_duracloud.setObjectName("vis_after_6_duracloud")
        self.vis_after_5_titanium = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after5="datasets\\After_preprocessing\\titanium.png"
        (self.vis_after_5_titanium).clicked.connect(lambda:os.system(self.after5)) ##############3########################33
        self.vis_after_5_titanium.setGeometry(QtCore.QRect(7, 148, 73, 21))
        self.vis_after_5_titanium.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_5_titanium.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_5_titanium.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_5_titanium.setObjectName("vis_after_5_titanium")
        self.vis_after_4_aptana = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after4="datasets\\After_preprocessing\\aptanastudio.png"
        (self.vis_after_4_aptana).clicked.connect(lambda:os.system(self.after4)) ##############3########################33
        self.vis_after_4_aptana.setGeometry(QtCore.QRect(7, 120, 73, 21))
        self.vis_after_4_aptana.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_4_aptana.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_4_aptana.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_4_aptana.setObjectName("vis_after_4_aptana")
        self.vis_after_3_appcelerator = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after3="datasets\\After_preprocessing\\appceleratorstudio.png"
        (self.vis_after_3_appcelerator).clicked.connect(lambda:os.system(self.after3)) ##############3########################33
        self.vis_after_3_appcelerator.setGeometry(QtCore.QRect(7, 91, 73, 21))
        self.vis_after_3_appcelerator.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_3_appcelerator.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_3_appcelerator.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_3_appcelerator.setObjectName("vis_after_3_appcelerator")
        self.vis_after_2_usergrid = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after2="datasets\\After_preprocessing\\usergrid.png"
        (self.vis_after_2_usergrid).clicked.connect(lambda:os.system(self.after2)) ##############3########################33
        self.vis_after_2_usergrid.setGeometry(QtCore.QRect(7, 64, 73, 21))
        self.vis_after_2_usergrid.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_2_usergrid.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_2_usergrid.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_2_usergrid.setObjectName("vis_after_2_usergrid")
        self.vis_after_16_talendesb = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after16="datasets\\After_preprocessing\\talendesb.png"
        (self.vis_after_16_talendesb).clicked.connect(lambda:os.system(self.after16)) ##############3########################33
        self.vis_after_16_talendesb.setGeometry(QtCore.QRect(7, 458, 73, 21))
        self.vis_after_16_talendesb.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_16_talendesb.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_16_talendesb.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_16_talendesb.setObjectName("vis_after_16_talendesb")
        self.vis_after_15_talenddata = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after15="datasets\\After_preprocessing\\talenddataquality.png"
        (self.vis_after_15_talenddata).clicked.connect(lambda:os.system(self.after15)) ##############3########################33
        self.vis_after_15_talenddata.setGeometry(QtCore.QRect(7, 429, 73, 21))
        self.vis_after_15_talenddata.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_15_talenddata.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_15_talenddata.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_15_talenddata.setObjectName("vis_after_15_talenddata")
        self.vis_after_14_spring = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after14="datasets\\After_preprocessing\\springxd.png"
        (self.vis_after_14_spring).clicked.connect(lambda:os.system(self.after14)) ##############3########################33
        self.vis_after_14_spring.setGeometry(QtCore.QRect(7, 399, 73, 21))
        self.vis_after_14_spring.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_14_spring.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_14_spring.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_14_spring.setObjectName("vis_after_14_spring")
        self.vis_after_13_mulestudio = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after13="datasets\\After_preprocessing\\mulestudio.png"
        (self.vis_after_13_mulestudio).clicked.connect(lambda:os.system(self.after13)) ##############3########################33
        self.vis_after_13_mulestudio.setGeometry(QtCore.QRect(7, 372, 73, 21))
        self.vis_after_13_mulestudio.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_13_mulestudio.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_13_mulestudio.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_13_mulestudio.setObjectName("vis_after_13_mulestudio")
        self.vis_after_12_mule = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after12="datasets\\After_preprocessing\\mule.png"
        (self.vis_after_12_mule).clicked.connect(lambda:os.system(self.after12)) ##############3########################33
        self.vis_after_12_mule.setGeometry(QtCore.QRect(7, 345, 73, 21))
        self.vis_after_12_mule.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_12_mule.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_12_mule.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_12_mule.setObjectName("vis_after_12_mule")
        self.vis_after_11_data = QtWidgets.QPushButton(self.frame_after_preprocess)
        self.after11="datasets\\After_preprocessing\\datamanagement.png"
        (self.vis_after_11_data).clicked.connect(lambda:os.system(self.after11)) ##############3########################33
        self.vis_after_11_data.setGeometry(QtCore.QRect(7, 317, 73, 21))
        self.vis_after_11_data.setMinimumSize(QtCore.QSize(73, 18))
        self.vis_after_11_data.setMaximumSize(QtCore.QSize(73, 21))
        self.vis_after_11_data.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(85, 152, 203);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgb(85, 152, 203,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.vis_after_11_data.setObjectName("vis_after_11_data")
        self.frame_all_show = QtWidgets.QFrame(self.frame_body)
        self.frame_all_show.setGeometry(QtCore.QRect(9, 508, 1257, 55))
        self.frame_all_show.setMinimumSize(QtCore.QSize(150, 55))
        self.frame_all_show.setMaximumSize(QtCore.QSize(16777215, 41))
        self.frame_all_show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_all_show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_all_show.setObjectName("frame_all_show")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_all_show)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_all_show)
        self.issue_pic="datasets\\Before_preprocessing\\issue_pic.png"
        (self.pushButton_3).clicked.connect(lambda:os.system(self.issue_pic))
        self.pushButton_3.setMinimumSize(QtCore.QSize(184, 40))
        self.pushButton_3.setMaximumSize(QtCore.QSize(184, 40))
        self.pushButton_3.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(182, 121, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(182, 121, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_all_show)
        self.before_preproceess_pic="datasets\\Before_preprocessing\\Visualization_before_preproceess.png"#########################
        (self.pushButton_2).clicked.connect(lambda:os.system(self.before_preproceess_pic))
        self.pushButton_2.setMinimumSize(QtCore.QSize(184, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(184, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(182, 121, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(182, 121, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_all_show)
        self.after_preproceess_pic="datasets\\After_preprocessing\\Visualization_after_preproceess.png"#########################
        (self.pushButton).clicked.connect(lambda:os.system(self.after_preproceess_pic))
        self.pushButton.setMinimumSize(QtCore.QSize(184, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(184, 40))
        self.pushButton.setStyleSheet("QPushButton{ \n"
"    border:5px sold rgb(60,231,195);\n"
"    background-color: rgb(182, 121, 0);\n"
"}\n"
" \n"
"QPushButton:hover{\n"
"    background-color: rgba(182, 121, 0,150);\n"
"    border:5px sold rgb(105, 95, 148);\n"
"} \n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.frame_exit_back = QtWidgets.QFrame(self.frame_body)
        self.frame_exit_back.setGeometry(QtCore.QRect(9, 571, 1257, 38))
        self.frame_exit_back.setMinimumSize(QtCore.QSize(0, 38))
        self.frame_exit_back.setMaximumSize(QtCore.QSize(16777215, 11))
        self.frame_exit_back.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_exit_back.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_exit_back.setObjectName("frame_exit_back")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_exit_back)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_back = QtWidgets.QPushButton(self.frame_exit_back)
        (self.pushButton_back).clicked.connect(lambda:MainWindow.hide()) ################################
        self.pushButton_back.setMinimumSize(QtCore.QSize(137, 30))
        self.pushButton_back.setMaximumSize(QtCore.QSize(137, 28))
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
        (self.pushButton_exit).clicked.connect(exit) ##############3#########################
        self.pushButton_exit.setMinimumSize(QtCore.QSize(137, 28))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(137, 28))
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
        self.dropshadow_layout_2.addWidget(self.backgrd_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Dataset Details"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "17"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Repo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Project"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "No of issues"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "min SP"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "max SP"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "mean SP"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "median SP"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "mode SP"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "var SP"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "std SP"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "mean TD length"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Apache"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Mesos"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "1,680"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("MainWindow", "40"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("MainWindow", "3.09"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(0, 8)
        item.setText(_translate("MainWindow", "5.87"))
        item = self.tableWidget.item(0, 9)
        item.setText(_translate("MainWindow", "2.42"))
        item = self.tableWidget.item(0, 10)
        item.setText(_translate("MainWindow", "181.12"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Apache"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Usergrid"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "482"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(1, 4)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(1, 5)
        item.setText(_translate("MainWindow", "2.85"))
        item = self.tableWidget.item(1, 6)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(1, 7)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(1, 8)
        item.setText(_translate("MainWindow", "1.97"))
        item = self.tableWidget.item(1, 9)
        item.setText(_translate("MainWindow", "1.4"))
        item = self.tableWidget.item(1, 10)
        item.setText(_translate("MainWindow", "108.6"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Appcelerator"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "Appcelerator Studio"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "2,919"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(2, 4)
        item.setText(_translate("MainWindow", "40"))
        item = self.tableWidget.item(2, 5)
        item.setText(_translate("MainWindow", "5.64"))
        item = self.tableWidget.item(2, 6)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(2, 7)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(2, 8)
        item.setText(_translate("MainWindow", "11.07"))
        item = self.tableWidget.item(2, 9)
        item.setText(_translate("MainWindow", "3.33"))
        item = self.tableWidget.item(2, 10)
        item.setText(_translate("MainWindow", "124.61"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "Appcelerator"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "Aptana Studio"))
        item = self.tableWidget.item(3, 2)
        item.setText(_translate("MainWindow", "829"))
        item = self.tableWidget.item(3, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(3, 4)
        item.setText(_translate("MainWindow", "40"))
        item = self.tableWidget.item(3, 5)
        item.setText(_translate("MainWindow", "8.02"))
        item = self.tableWidget.item(3, 6)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(3, 7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(3, 8)
        item.setText(_translate("MainWindow", "35.46"))
        item = self.tableWidget.item(3, 9)
        item.setText(_translate("MainWindow", "5.95"))
        item = self.tableWidget.item(3, 10)
        item.setText(_translate("MainWindow", "124.61"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Appcelerator"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "Titanium SDK/CLI"))
        item = self.tableWidget.item(4, 2)
        item.setText(_translate("MainWindow", "2,251"))
        item = self.tableWidget.item(4, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(4, 4)
        item.setText(_translate("MainWindow", "34"))
        item = self.tableWidget.item(4, 5)
        item.setText(_translate("MainWindow", "6.32"))
        item = self.tableWidget.item(4, 6)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(4, 7)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(4, 8)
        item.setText(_translate("MainWindow", "25.97"))
        item = self.tableWidget.item(4, 9)
        item.setText(_translate("MainWindow", "5.1"))
        item = self.tableWidget.item(4, 10)
        item.setText(_translate("MainWindow", "2.05.9"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "DuraSpace"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "DuraCloud"))
        item = self.tableWidget.item(5, 2)
        item.setText(_translate("MainWindow", "666"))
        item = self.tableWidget.item(5, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(5, 4)
        item.setText(_translate("MainWindow", "16"))
        item = self.tableWidget.item(5, 5)
        item.setText(_translate("MainWindow", "2.13"))
        item = self.tableWidget.item(5, 6)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(5, 7)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(5, 8)
        item.setText(_translate("MainWindow", "4.12"))
        item = self.tableWidget.item(5, 9)
        item.setText(_translate("MainWindow", "2.03"))
        item = self.tableWidget.item(5, 10)
        item.setText(_translate("MainWindow", "70.91"))
        item = self.tableWidget.item(6, 0)
        item.setText(_translate("MainWindow", "Atlassian"))
        item = self.tableWidget.item(6, 1)
        item.setText(_translate("MainWindow", "Bamboo"))
        item = self.tableWidget.item(6, 2)
        item.setText(_translate("MainWindow", "521"))
        item = self.tableWidget.item(6, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(6, 4)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget.item(6, 5)
        item.setText(_translate("MainWindow", "2.42"))
        item = self.tableWidget.item(6, 6)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(6, 7)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(6, 8)
        item.setText(_translate("MainWindow", "4.6"))
        item = self.tableWidget.item(6, 9)
        item.setText(_translate("MainWindow", "2.14"))
        item = self.tableWidget.item(6, 10)
        item.setText(_translate("MainWindow", "133.28"))
        item = self.tableWidget.item(7, 0)
        item.setText(_translate("MainWindow", "Atlassian"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainWindow", "Clover"))
        item = self.tableWidget.item(7, 2)
        item.setText(_translate("MainWindow", "384"))
        item = self.tableWidget.item(7, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(7, 4)
        item.setText(_translate("MainWindow", "40"))
        item = self.tableWidget.item(7, 5)
        item.setText(_translate("MainWindow", "4.59"))
        item = self.tableWidget.item(7, 6)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(7, 7)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(7, 8)
        item.setText(_translate("MainWindow", "42.95"))
        item = self.tableWidget.item(7, 9)
        item.setText(_translate("MainWindow", "6.55"))
        item = self.tableWidget.item(7, 10)
        item.setText(_translate("MainWindow", "124.48"))
        item = self.tableWidget.item(8, 0)
        item.setText(_translate("MainWindow", "Atlassian"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainWindow", "JIRA Software"))
        item = self.tableWidget.item(8, 2)
        item.setText(_translate("MainWindow", "352"))
        item = self.tableWidget.item(8, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(8, 4)
        item.setText(_translate("MainWindow", "20"))
        item = self.tableWidget.item(8, 5)
        item.setText(_translate("MainWindow", "4.43"))
        item = self.tableWidget.item(8, 6)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(8, 7)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(8, 8)
        item.setText(_translate("MainWindow", "12.35"))
        item = self.tableWidget.item(8, 9)
        item.setText(_translate("MainWindow", "3.51"))
        item = self.tableWidget.item(8, 10)
        item.setText(_translate("MainWindow", "114.57"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "Moodle"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainWindow", "Moodle"))
        item = self.tableWidget.item(9, 2)
        item.setText(_translate("MainWindow", "1,166"))
        item = self.tableWidget.item(9, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(9, 4)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(9, 5)
        item.setText(_translate("MainWindow", "15.54"))
        item = self.tableWidget.item(9, 6)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(9, 7)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(9, 8)
        item.setText(_translate("MainWindow", "468.53"))
        item = self.tableWidget.item(9, 9)
        item.setText(_translate("MainWindow", "21.65"))
        item = self.tableWidget.item(9, 10)
        item.setText(_translate("MainWindow", "88.86"))
        item = self.tableWidget.item(10, 0)
        item.setText(_translate("MainWindow", "Lsstcorp"))
        item = self.tableWidget.item(10, 1)
        item.setText(_translate("MainWindow", "Data Management"))
        item = self.tableWidget.item(10, 2)
        item.setText(_translate("MainWindow", "4,667"))
        item = self.tableWidget.item(10, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(10, 4)
        item.setText(_translate("MainWindow", "100"))
        item = self.tableWidget.item(10, 5)
        item.setText(_translate("MainWindow", "9.57"))
        item = self.tableWidget.item(10, 6)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.item(10, 7)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(10, 8)
        item.setText(_translate("MainWindow", "275.71"))
        item = self.tableWidget.item(10, 9)
        item.setText(_translate("MainWindow", "16.61"))
        item = self.tableWidget.item(10, 10)
        item.setText(_translate("MainWindow", "69.41"))
        item = self.tableWidget.item(11, 0)
        item.setText(_translate("MainWindow", "Mulesoft"))
        item = self.tableWidget.item(11, 1)
        item.setText(_translate("MainWindow", "Mule"))
        item = self.tableWidget.item(11, 2)
        item.setText(_translate("MainWindow", "889"))
        item = self.tableWidget.item(11, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(11, 4)
        item.setText(_translate("MainWindow", "21"))
        item = self.tableWidget.item(11, 5)
        item.setText(_translate("MainWindow", "5.08"))
        item = self.tableWidget.item(11, 6)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(11, 7)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(11, 8)
        item.setText(_translate("MainWindow", "12.24"))
        item = self.tableWidget.item(11, 9)
        item.setText(_translate("MainWindow", "3.5"))
        item = self.tableWidget.item(11, 10)
        item.setText(_translate("MainWindow", "81.16"))
        item = self.tableWidget.item(12, 0)
        item.setText(_translate("MainWindow", "Mulesoft"))
        item = self.tableWidget.item(12, 1)
        item.setText(_translate("MainWindow", "Mule Studio"))
        item = self.tableWidget.item(12, 2)
        item.setText(_translate("MainWindow", "732"))
        item = self.tableWidget.item(12, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(12, 4)
        item.setText(_translate("MainWindow", "34"))
        item = self.tableWidget.item(12, 5)
        item.setText(_translate("MainWindow", "6.4"))
        item = self.tableWidget.item(12, 6)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(12, 7)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(12, 8)
        item.setText(_translate("MainWindow", "29.01"))
        item = self.tableWidget.item(12, 9)
        item.setText(_translate("MainWindow", "5.39"))
        item = self.tableWidget.item(12, 10)
        item.setText(_translate("MainWindow", "70.99"))
        item = self.tableWidget.item(13, 0)
        item.setText(_translate("MainWindow", "Spring"))
        item = self.tableWidget.item(13, 1)
        item.setText(_translate("MainWindow", "Spring XD"))
        item = self.tableWidget.item(13, 2)
        item.setText(_translate("MainWindow", "3,526"))
        item = self.tableWidget.item(13, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(13, 4)
        item.setText(_translate("MainWindow", "40"))
        item = self.tableWidget.item(13, 5)
        item.setText(_translate("MainWindow", "3.7"))
        item = self.tableWidget.item(13, 6)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(13, 7)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(13, 8)
        item.setText(_translate("MainWindow", "10.42"))
        item = self.tableWidget.item(13, 9)
        item.setText(_translate("MainWindow", "3.23"))
        item = self.tableWidget.item(13, 10)
        item.setText(_translate("MainWindow", "78.47"))
        item = self.tableWidget.item(14, 0)
        item.setText(_translate("MainWindow", "Talendforge"))
        item = self.tableWidget.item(14, 1)
        item.setText(_translate("MainWindow", "Talend Data Quality"))
        item = self.tableWidget.item(14, 2)
        item.setText(_translate("MainWindow", "1,381"))
        item = self.tableWidget.item(14, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(14, 4)
        item.setText(_translate("MainWindow", "40"))
        item = self.tableWidget.item(14, 5)
        item.setText(_translate("MainWindow", "5.92"))
        item = self.tableWidget.item(14, 6)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.item(14, 7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.item(14, 8)
        item.setText(_translate("MainWindow", "26.96"))
        item = self.tableWidget.item(14, 9)
        item.setText(_translate("MainWindow", "5.19"))
        item = self.tableWidget.item(14, 10)
        item.setText(_translate("MainWindow", "104.86"))
        item = self.tableWidget.item(15, 0)
        item.setText(_translate("MainWindow", "Talendforge"))
        item = self.tableWidget.item(15, 1)
        item.setText(_translate("MainWindow", "Talend ESB"))
        item = self.tableWidget.item(15, 2)
        item.setText(_translate("MainWindow", "868"))
        item = self.tableWidget.item(15, 3)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(15, 4)
        item.setText(_translate("MainWindow", "13"))
        item = self.tableWidget.item(15, 5)
        item.setText(_translate("MainWindow", "2.16"))
        item = self.tableWidget.item(15, 6)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.item(15, 7)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.item(15, 8)
        item.setText(_translate("MainWindow", "2.24"))
        item = self.tableWidget.item(15, 9)
        item.setText(_translate("MainWindow", "1.5"))
        item = self.tableWidget.item(15, 10)
        item.setText(_translate("MainWindow", "128.97"))
        item = self.tableWidget.item(16, 0)
        item.setText(_translate("MainWindow", "Total"))
        item = self.tableWidget.item(16, 2)
        item.setText(_translate("MainWindow", "23,313"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_dataset_view.setText(_translate("MainWindow", "View Dataset"))
        self.dataset_view_1_mesos.setText(_translate("MainWindow", "view 1"))
        self.dataset_view_2_usergrid.setText(_translate("MainWindow", "view 2"))
        self.dataset_view_3_appcelerator.setText(_translate("MainWindow", "view 3"))
        self.dataset_view_4_aptana.setText(_translate("MainWindow", "view 4"))
        self.dataset_view_5_titanium.setText(_translate("MainWindow", " view 5"))
        self.dataset_view_6_duracloud.setText(_translate("MainWindow", "view 6"))
        self.dataset_view_12_mule.setText(_translate("MainWindow", "view 12"))
        self.dataset_view_11_data.setText(_translate("MainWindow", "view 11"))
        self.dataset_view_10_moodle.setText(_translate("MainWindow", "view 10"))
        self.dataset_view_9_jira.setText(_translate("MainWindow", "view 9 "))
        self.dataset_view_8_clover.setText(_translate("MainWindow", "view 8"))
        self.dataset_view_7_bamboo.setText(_translate("MainWindow", "view 7"))
        self.dataset_view_16_talendesb.setText(_translate("MainWindow", "view 16"))
        self.dataset_view_15_talenddata.setText(_translate("MainWindow", "view 15"))
        self.dataset_view_14_spring.setText(_translate("MainWindow", "view 14"))
        self.dataset_view_13_mulestudio.setText(_translate("MainWindow", "view 13"))
        self.label_2.setText(_translate("MainWindow", "  Visualise  (Before ..preprocessing)"))
        self.vis_before_1_mesos.setText(_translate("MainWindow", "view 1"))
        self.vis_before_2_usergrid.setText(_translate("MainWindow", "view 2"))
        self.vis_before_3_appcelerator.setText(_translate("MainWindow", "view 3"))
        self.vis_before_4_aptana.setText(_translate("MainWindow", "view 4"))
        self.vis_before_5_titanium.setText(_translate("MainWindow", "view 5"))
        self.vis_before_6_duracloud.setText(_translate("MainWindow", "view 6"))
        self.vis_before_7_bamboo.setText(_translate("MainWindow", "view 7"))
        self.vis_before_8_clover.setText(_translate("MainWindow", "view 8"))
        self.vis_before_9_jira.setText(_translate("MainWindow", "view 9 "))
        self.vis_before_10_moodle.setText(_translate("MainWindow", "view 10"))
        self.vis_before_16_talendesb.setText(_translate("MainWindow", "view 16"))
        self.vis_before_15_talenddata.setText(_translate("MainWindow", "view 15"))
        self.vis_before_14_spring.setText(_translate("MainWindow", "view 14"))
        self.vis_before_13_mulestudio.setText(_translate("MainWindow", "view 13"))
        self.vis_before_12_mule.setText(_translate("MainWindow", "view 12"))
        self.vis_before_11_data.setText(_translate("MainWindow", "view 11"))
        self.label_3.setText(_translate("MainWindow", "  Visualise  (After ..preprocessing)"))
        self.vis_after_1_mesos.setText(_translate("MainWindow", "view 1"))
        self.vis_after_10_moodle.setText(_translate("MainWindow", "view 10"))
        self.vis_after_9_jira.setText(_translate("MainWindow", "view 9 "))
        self.vis_after_8_clover.setText(_translate("MainWindow", "view 8"))
        self.vis_after_7_bamboo.setText(_translate("MainWindow", "view 7"))
        self.vis_after_6_duracloud.setText(_translate("MainWindow", "view 6"))
        self.vis_after_5_titanium.setText(_translate("MainWindow", "view 5"))
        self.vis_after_4_aptana.setText(_translate("MainWindow", "view 4"))
        self.vis_after_3_appcelerator.setText(_translate("MainWindow", "view 3"))
        self.vis_after_2_usergrid.setText(_translate("MainWindow", "view 2"))
        self.vis_after_16_talendesb.setText(_translate("MainWindow", "view 16"))
        self.vis_after_15_talenddata.setText(_translate("MainWindow", "view 15"))
        self.vis_after_14_spring.setText(_translate("MainWindow", "view 14"))
        self.vis_after_13_mulestudio.setText(_translate("MainWindow", "view 13"))
        self.vis_after_12_mule.setText(_translate("MainWindow", "view 12"))
        self.vis_after_11_data.setText(_translate("MainWindow", "view 11"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "click here"))
        self.pushButton_3.setText(_translate("MainWindow", "View Issue Sample"))
        self.pushButton_2.setToolTip(_translate("MainWindow", "click here"))
        self.pushButton_2.setText(_translate("MainWindow", "view complete dataset (Before \n"
"Preprocessing)"))
        self.pushButton.setToolTip(_translate("MainWindow", "click here"))
        self.pushButton.setText(_translate("MainWindow", "view complete dataset (After \n"
"Preprocessing)"))
        self.pushButton_back.setToolTip(_translate("MainWindow", "click here"))
        self.pushButton_back.setText(_translate("MainWindow", "Back to Home Window"))
        self.pushButton_exit.setToolTip(_translate("MainWindow", "click here"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit Application"))

    
        
    

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_dataset_details()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''
