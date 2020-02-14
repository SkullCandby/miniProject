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
        MapsApp.resize(982, 600)
        self.centralwidget = QtWidgets.QWidget(MapsApp)
        self.centralwidget.setObjectName("centralwidget")
        self._width = QtWidgets.QLineEdit(self.centralwidget)
        self._width.setGeometry(QtCore.QRect(68, 22, 133, 20))
        self._width.setObjectName("_width")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(22, 22, 40, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(209, 22, 43, 16))
        self.label_2.setObjectName("label_2")
        self.length = QtWidgets.QLineEdit(self.centralwidget)
        self.length.setGeometry(QtCore.QRect(258, 22, 133, 20))
        self.length.setObjectName("length")
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MapsApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MapsApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 21))
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
        self.label.setText(_translate("MapsApp", "Широта"))
        self.label_2.setText(_translate("MapsApp", "Долгота"))
        self.label_3.setText(_translate("MapsApp", "Протяжённость по долготе"))
        self.label_4.setText(_translate("MapsApp", "Протяжённость по долготе"))
        self.pushButton.setText(_translate("MapsApp", "go"))
