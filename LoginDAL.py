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
        
        self.loginButton = self.findChild(QtWidgets.QPushButton,'loginButton')
        self.registerButton = self.findChild(QtWidgets.QPushButton,'registerButton')
        self.usernameLine = self.findChild(QtWidgets.QLineEdit,'userLine')
        self.passwordLine = self.findChild(QtWidgets.QLineEdit,'passLine')
        

    def login(self):
        logacc = Account()
        logacc.setUsername(self.usernameLine.text())
        logacc.setPassword(self.passwordLine.text())
        value = loginProcess(self,logacc)
       

#CLASS FOR THE REGISTER UI
class registerUi(QtWidgets.QWidget):
    def __init__(self):
        super(registerUi,self).__init__()
        uic.loadUi("registerGui.ui",self)
        
        
    def reg(self):
        acc = Account()
        acc.setUsername(self.newuserline.text())
        acc.setPassword(self.newpassline.text())
        acc.setfName(self.newfnameline.text())
        acc.setlName(self.newlnameline.text())
        
        if acc.username.__len__() <= 0 or acc.username == " " or acc.password.__len__() <= 0 or acc.password == " " or acc.fname.__len__() <= 0 or acc.fname == " " or acc.lname.__len__() <= 0 or acc.lname == " " :
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            
            mess.setText("Cannot accept blank inputs")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()
        else:
            self.newuserline.clear()
            self.newpassline.clear()
            self.newfnameline.clear()
            self.newlnameline.clear()
            if(registerAcc(self,acc)):
                
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Information)
            
                mess.setText("Registration successful!")
                mess.setWindowTitle("Register")
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec()     
                
                
                self.close()
            else:
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Information)
                mess.setText("Please make sure inputs are correct!")
                mess.setWindowTitle("Input error")
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec()    
            
class selectUi(QtWidgets.QWidget):
    def __init__(self):
        super(selectGui,self).__init__()
        uic.loadUi('sel.ui',self)
       
    def learning(self):
        os.system('python objectdetectionimage.py')
    def network(self):
        os.system('python objectdetectionimagewebcam.py')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = loginUi()
    window.show()
    sys.exit(app.exec_())
