# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from auth import Account
from auth import registerAcc
from PyQt5.QtWidgets import QMessageBox 

class Ui_regForm(object):
    def setupUi(self, regForm):
        regForm.setObjectName("regForm")
        regForm.resize(303, 238)
        self.userLine = QtWidgets.QLineEdit(regForm)
        self.userLine.setGeometry(QtCore.QRect(100, 20, 151, 20))
        self.userLine.setObjectName("userLine")
        self.passLine = QtWidgets.QLineEdit(regForm)
        self.passLine.setGeometry(QtCore.QRect(100, 50, 151, 21))
        self.passLine.setObjectName("passLine")
        self.fnameLine = QtWidgets.QLineEdit(regForm)
        self.fnameLine.setGeometry(QtCore.QRect(100, 80, 151, 21))
        self.fnameLine.setObjectName("fnameLine")
        self.lnameLine = QtWidgets.QLineEdit(regForm)
        self.lnameLine.setGeometry(QtCore.QRect(100, 110, 151, 21))
        self.lnameLine.setObjectName("lnameLine")
        self.registerButton = QtWidgets.QPushButton(regForm)
        self.registerButton.setGeometry(QtCore.QRect(150, 150, 101, 41))
        self.registerButton.setObjectName("registerButton")
        self.cancelButton = QtWidgets.QPushButton(regForm)
        self.cancelButton.setGeometry(QtCore.QRect(30, 150, 101, 41))
        self.cancelButton.setObjectName("cancelButton")
        self.userLabel = QtWidgets.QLabel(regForm)
        self.userLabel.setGeometry(QtCore.QRect(30, 15, 71, 31))
        self.userLabel.setObjectName("userLabel")
        self.passwordLabel = QtWidgets.QLabel(regForm)
        self.passwordLabel.setGeometry(QtCore.QRect(30, 50, 61, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        self.fnameLabel = QtWidgets.QLabel(regForm)
        self.fnameLabel.setGeometry(QtCore.QRect(30, 80, 71, 21))
        self.fnameLabel.setObjectName("fnameLabel")
        self.lnameLabel = QtWidgets.QLabel(regForm)
        self.lnameLabel.setGeometry(QtCore.QRect(30, 110, 61, 16))
        self.lnameLabel.setObjectName("lnameLabel")
        
        self.registerButton.clicked.connect(self.register)
        self.retranslateUi(regForm)
        QtCore.QMetaObject.connectSlotsByName(regForm)
        
    def register(self):
        acc = Account()
        acc.setUsername(self.userLine.text())
        acc.setPassword(self.passLine.text())
        acc.setfName(self.fnameLine.text())
        acc.setlName(self.lnameLine.text())
        
        if acc.username.__len__() <= 0 or acc.username == " " or acc.password.__len__() <= 0 or acc.password == " " or acc.fname.__len__() <= 0 or acc.fname == " " or acc.lname.__len__() <= 0 or acc.lname == " " :
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            
            mess.setText("Cannot accept blank inputs")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()
        else:
            self.userLine.clear()
            self.passLine.clear()
            self.fnameLine.clear()
            self.lnameLine.clear()
            val = registerAcc(self,acc)
            
def retranslateUi(self, regForm):
        _translate = QtCore.QCoreApplication.translate
        regForm.setWindowTitle(_translate("regForm", "Registration"))
        self.registerButton.setText(_translate("regForm", "Register"))
        self.cancelButton.setText(_translate("regForm", "Cancel"))
        self.userLabel.setText(_translate("regForm", "Username:"))
        self.passwordLabel.setText(_translate("regForm", "Password:"))
        self.fnameLabel.setText(_translate("regForm", "First Name:"))
        self.lnameLabel.setText(_translate("regForm", "Last Name:"))

   






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regForm = QtWidgets.QWidget()
    ui = Ui_regForm()
    ui.setupUi(regForm)
    regForm.show()
    sys.exit(app.exec_())

