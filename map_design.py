# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'map_design.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MapsApp(object):
    def setupUi(self, MapsApp):
        MapsApp.setObjectName("MapsApp")
        MapsApp.resize(959, 600)
        self.centralwidget = QtWidgets.QWidget(MapsApp)
        self.centralwidget.setObjectName("centralwidget")
        self.lenght_size = QtWidgets.QLineEdit(self.centralwidget)
        self.lenght_size.setGeometry(QtCore.QRect(807, 21, 71, 20))
        self.lenght_size.setObjectName("lenght_size")
        self.width_size = QtWidgets.QLineEdit(self.centralwidget)
        self.width_size.setGeometry(QtCore.QRect(577, 21, 71, 20))
        self.width_size.setObjectName("width_size")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(431, 21, 140, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(661, 21, 140, 16))
        self.label_4.setObjectName("label_4")
        self.img_lbl = QtWidgets.QLabel(self.centralwidget)
        self.img_lbl.setGeometry(QtCore.QRect(20, 60, 911, 491))
        self.img_lbl.setText("")
        self.img_lbl.setObjectName("img_lbl")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 373, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.width = QtWidgets.QLineEdit(self.widget)
        self.width.setObjectName("width")
        self.horizontalLayout.addWidget(self.width)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.length = QtWidgets.QLineEdit(self.widget)
        self.length.setObjectName("length")
        self.horizontalLayout_2.addWidget(self.length)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        MapsApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapsApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 21))
        self.menubar.setObjectName("menubar")
        MapsApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MapsApp)
        self.statusbar.setObjectName("statusbar")
        MapsApp.setStatusBar(self.statusbar)

        self.retranslateUi(MapsApp)
        QtCore.QMetaObject.connectSlotsByName(MapsApp)

    def retranslateUi(self, MapsApp):
        _translate = QtCore.QCoreApplication.translate
        MapsApp.setWindowTitle(_translate("MapsApp", "MainWindow"))
        self.label_3.setText(_translate("MapsApp", "Протяжённость по долготе"))
        self.label_4.setText(_translate("MapsApp", "Протяжённость по долготе"))
        self.label.setText(_translate("MapsApp", "Широта"))
        self.label_2.setText(_translate("MapsApp", "Долгота"))
