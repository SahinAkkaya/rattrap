# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rattrap.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Rattrap(object):
    def setupUi(self, Rattrap):
        Rattrap.setObjectName("Rattrap")
        Rattrap.resize(398, 522)
        self.centralwidget = QtWidgets.QWidget(Rattrap)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_mode = QtWidgets.QLabel(self.widget)
        self.label_mode.setObjectName("label_mode")
        self.horizontalLayout_8.addWidget(self.label_mode)
        self.radiobtn_mode1 = QtWidgets.QRadioButton(self.widget)
        self.radiobtn_mode1.setEnabled(False)
        self.radiobtn_mode1.setObjectName("radiobtn_mode1")
        self.horizontalLayout_8.addWidget(self.radiobtn_mode1)
        self.radiobtn_mode2 = QtWidgets.QRadioButton(self.widget)
        self.radiobtn_mode2.setEnabled(False)
        self.radiobtn_mode2.setObjectName("radiobtn_mode2")
        self.horizontalLayout_8.addWidget(self.radiobtn_mode2)
        self.radiobtn_mode3 = QtWidgets.QRadioButton(self.widget)
        self.radiobtn_mode3.setEnabled(False)
        self.radiobtn_mode3.setObjectName("radiobtn_mode3")
        self.horizontalLayout_8.addWidget(self.radiobtn_mode3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_color = QtWidgets.QLabel(self.widget)
        self.label_color.setObjectName("label_color")
        self.horizontalLayout_3.addWidget(self.label_color)
        self.color = QtWidgets.QComboBox(self.widget)
        self.color.setObjectName("color")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.color.addItem("")
        self.horizontalLayout_3.addWidget(self.color)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_left = QtWidgets.QLabel(self.widget)
        self.label_left.setObjectName("label_left")
        self.horizontalLayout_5.addWidget(self.label_left)
        self.left = QtWidgets.QPushButton(self.widget)
        self.left.setObjectName("left")
        self.horizontalLayout_5.addWidget(self.left)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_right = QtWidgets.QLabel(self.widget)
        self.label_right.setObjectName("label_right")
        self.horizontalLayout_4.addWidget(self.label_right)
        self.right = QtWidgets.QPushButton(self.widget)
        self.right.setObjectName("right")
        self.horizontalLayout_4.addWidget(self.right)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_middle = QtWidgets.QLabel(self.widget)
        self.label_middle.setObjectName("label_middle")
        self.horizontalLayout_7.addWidget(self.label_middle)
        self.middle = QtWidgets.QPushButton(self.widget)
        self.middle.setObjectName("middle")
        self.horizontalLayout_7.addWidget(self.middle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_g4 = QtWidgets.QLabel(self.widget)
        self.label_g4.setObjectName("label_g4")
        self.horizontalLayout_9.addWidget(self.label_g4)
        self.g4 = QtWidgets.QPushButton(self.widget)
        self.g4.setObjectName("g4")
        self.horizontalLayout_9.addWidget(self.g4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_g5 = QtWidgets.QLabel(self.widget)
        self.label_g5.setObjectName("label_g5")
        self.horizontalLayout_2.addWidget(self.label_g5)
        self.g5 = QtWidgets.QPushButton(self.widget)
        self.g5.setObjectName("g5")
        self.horizontalLayout_2.addWidget(self.g5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_g6 = QtWidgets.QLabel(self.widget)
        self.label_g6.setObjectName("label_g6")
        self.horizontalLayout_6.addWidget(self.label_g6)
        self.g6 = QtWidgets.QPushButton(self.widget)
        self.g6.setObjectName("g6")
        self.horizontalLayout_6.addWidget(self.g6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_g7 = QtWidgets.QLabel(self.widget)
        self.label_g7.setObjectName("label_g7")
        self.horizontalLayout_10.addWidget(self.label_g7)
        self.g7 = QtWidgets.QPushButton(self.widget)
        self.g7.setObjectName("g7")
        self.horizontalLayout_10.addWidget(self.g7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_g8 = QtWidgets.QLabel(self.widget)
        self.label_g8.setObjectName("label_g8")
        self.horizontalLayout_11.addWidget(self.label_g8)
        self.g8 = QtWidgets.QPushButton(self.widget)
        self.g8.setObjectName("g8")
        self.horizontalLayout_11.addWidget(self.g8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_g9 = QtWidgets.QLabel(self.widget)
        self.label_g9.setObjectName("label_g9")
        self.horizontalLayout_12.addWidget(self.label_g9)
        self.g9 = QtWidgets.QPushButton(self.widget)
        self.g9.setObjectName("g9")
        self.horizontalLayout_12.addWidget(self.g9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.button_apply = QtWidgets.QPushButton(self.widget)
        self.button_apply.setEnabled(False)
        self.button_apply.setObjectName("button_apply")
        self.verticalLayout_3.addWidget(self.button_apply)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.widget)
        Rattrap.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Rattrap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 398, 20))
        self.menubar.setObjectName("menubar")
        Rattrap.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Rattrap)
        self.statusbar.setObjectName("statusbar")
        Rattrap.setStatusBar(self.statusbar)

        self.retranslateUi(Rattrap)
        QtCore.QMetaObject.connectSlotsByName(Rattrap)

    def retranslateUi(self, Rattrap):
        _translate = QtCore.QCoreApplication.translate
        Rattrap.setWindowTitle(_translate("Rattrap", "MainWindow"))
        self.label_mode.setText(_translate("Rattrap", "Mode"))
        self.radiobtn_mode1.setText(_translate("Rattrap", "1"))
        self.radiobtn_mode2.setText(_translate("Rattrap", "2"))
        self.radiobtn_mode3.setText(_translate("Rattrap", "3"))
        self.label_color.setText(_translate("Rattrap", "Color"))
        self.color.setItemText(0, _translate("Rattrap", "Black"))
        self.color.setItemText(1, _translate("Rattrap", "Blue"))
        self.color.setItemText(2, _translate("Rattrap", "Cyan"))
        self.color.setItemText(3, _translate("Rattrap", "Red"))
        self.color.setItemText(4, _translate("Rattrap", "Magenta"))
        self.color.setItemText(5, _translate("Rattrap", "Yellow"))
        self.color.setItemText(6, _translate("Rattrap", "White"))
        self.color.setItemText(7, _translate("Rattrap", "Green"))
        self.label_left.setText(_translate("Rattrap", "Left"))
        self.left.setText(_translate("Rattrap", "Not Defined"))
        self.label_right.setText(_translate("Rattrap", "Right"))
        self.right.setText(_translate("Rattrap", "Not Defined"))
        self.label_middle.setText(_translate("Rattrap", "Middle"))
        self.middle.setText(_translate("Rattrap", "Not Defined"))
        self.label_g4.setText(_translate("Rattrap", "G4"))
        self.g4.setText(_translate("Rattrap", "Not Defined"))
        self.label_g5.setText(_translate("Rattrap", "G5"))
        self.g5.setText(_translate("Rattrap", "Not Defined"))
        self.label_g6.setText(_translate("Rattrap", "G6"))
        self.g6.setText(_translate("Rattrap", "Not Defined"))
        self.label_g7.setText(_translate("Rattrap", "G7"))
        self.g7.setText(_translate("Rattrap", "Not Defined"))
        self.label_g8.setText(_translate("Rattrap", "G8"))
        self.g8.setText(_translate("Rattrap", "Not Defined"))
        self.label_g9.setText(_translate("Rattrap", "G9"))
        self.g9.setText(_translate("Rattrap", "Not Defined"))
        self.button_apply.setText(_translate("Rattrap", "Apply Changes!"))

