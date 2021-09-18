# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui01.ui'
#
# Created: Sun Feb 25 16:07:21 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def __init__(self, defulte01=1, defulte02=2):
        self.defulteA = defulte01
        self.defulteB = defulte02

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 428)
        self.textBrowser01 = QtWidgets.QTextBrowser(Form)
        self.textBrowser01.setGeometry(QtCore.QRect(10, 170, 421, 191))
        self.textBrowser01.setObjectName("textBrowser01")
        self.textinput01 = QtWidgets.QTextEdit(Form)
        self.textinput01.setGeometry(QtCore.QRect(10, 60, 421, 91))
        self.textinput01.setObjectName("textinput01")
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setGeometry(QtCore.QRect(570, 380, 99, 27))
        self.ExitButton.setObjectName("ExitButton")
        self.CleareButton01 = QtWidgets.QPushButton(Form)
        self.CleareButton01.setGeometry(QtCore.QRect(340, 370, 99, 27))
        self.CleareButton01.setObjectName("CleareButton01")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 110, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)

        self.Num = "num : " + self.defulteA.__str__() + "\nName :" + self.defulteB.__str__()

        self.textBrowser01.setText(self.Num.__str__())

        self.CleareButton01.clicked.connect(self.textBrowser01.clear)
        self.pushButton_2.clicked.connect(self.textinput01.copy)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ExitButton.setText(_translate("Form", "Exit"))
        self.CleareButton01.setText(_translate("Form", "Cleare"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

    def runThis(self):
        import sys


        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        self.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())





