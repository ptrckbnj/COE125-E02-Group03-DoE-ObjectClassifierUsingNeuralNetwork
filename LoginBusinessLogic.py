# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox 

#from reglay import registerUi
from auth import Account
from auth import loginProcess 
from auth import registerAcc
import os
#from selectpy import selectUi

import bgi
import sys

class loginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginUi,self).__init__()
        uic.loadUi("loginGui.ui",self)
		
		
        self.loginButton.clicked.connect(self.login)
        self.registerButton.clicked.connect(self.reg)
        
        self.show()
         
    def login(self):
        
        if value is True: 
            self.selui = selectUi()
            self.selui.show()
            self.close()
        
        else:
            self.usernameLine.clear()
            self.passwordLine.clear()
                   
    def reg(self):
        self.regui = registerUi()
        self.regui.show()
#CLASS FOR THE REGISTER UI
class registerUi(QtWidgets.QWidget):
    def __init__(self):
        super(registerUi,self).__init__()
        uic.loadUi("registerGui.ui",self)
        
        self.newuserline = self.findChild(QtWidgets.QLineEdit,'userLine')
        self.newpassline = self.findChild(QtWidgets.QLineEdit,'passLine')
        self.newfnameline = self.findChild(QtWidgets.QLineEdit,'fnameLine')
        self.newlnameline = self.findChild(QtWidgets.QLineEdit,'lnameLine')
        
        self.regButton = self.findChild(QtWidgets.QPushButton,'registerButton')
        self.canButton = self.findChild(QtWidgets.QPushButton,'cancelButton')
        
        self.regButton.clicked.connect(self.reg)
        self.canButton.clicked.connect(self.can)
        
        self.show()
        
    def can(self):
        self.close()
        
   
            
class selectUi(QtWidgets.QWidget):
    def __init__(self):
        super(selectUi,self).__init__()
        uic.loadUi('selectGui.ui',self)
        self.learnBut = self.findChild(QtWidgets.QPushButton,"learningButton")
        self.netBut = self.findChild(QtWidgets.QPushButton,"networkButton")
        
        self.learnBut.clicked.connect(self.learning)
        self.netBut.clicked.connect(self.network)
        
        self.show()
    def learning(self):
        
    def network(self):
        os.system('python objectdetectionimagewebcam.py')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = loginUi()
    window.show()
    sys.exit(app.exec_())
