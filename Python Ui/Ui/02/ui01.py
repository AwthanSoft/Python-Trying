# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui02.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):

    def __init__(self, defulte01 = 1 , defulte02 = 2):
        self.defulteA = defulte01
        self.defulteB = defulte02

    def setupUi(self, Form ):




        Form.setObjectName("Form")
        Form.resize(1891, 1353)
        self.pushButton01 = QtWidgets.QPushButton(Form)
        self.pushButton01.setGeometry(QtCore.QRect(1210, 270, 461, 151))
        self.pushButton01.setObjectName("pushButton01")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(160, 130, 801, 481))
        self.textEdit.setObjectName("textEdit")
        self.pushButton02 = QtWidgets.QPushButton(Form)
        self.pushButton02.setGeometry(QtCore.QRect(1230, 670, 461, 151))
        self.pushButton02.setObjectName("pushButton02")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 760, 801, 481))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)


        self.textEdit.setText(self.defulteA.__str__())
        self.textEdit_2.setText(self.defulteB.__str__())


        self.pushButton01.clicked.connect(self.textEdit.selectAll)
        self.pushButton01.clicked.connect(self.textEdit.copy)
        self.pushButton02.clicked.connect(self.textEdit_2.paste)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pushButton01, self.textEdit)




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton01.setText(_translate("Form", "but 01"))
        self.pushButton02.setText(_translate("Form", "but 02"))

    def runThis(self):
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()

        self.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
  #  ui.textEdit.setText(ui.defulteA)
    Form.show()
    sys.exit(app.exec_())

