# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginLayout.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from auth import Account
from auth import loginProcess 


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(352, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userLine = QtWidgets.QLineEdit(self.centralwidget)
        self.userLine.setGeometry(QtCore.QRect(126, 30, 161, 31))
        self.userLine.setObjectName("userLine")
        self.passLine = QtWidgets.QLineEdit(self.centralwidget)
        self.passLine.setGeometry(QtCore.QRect(126, 80, 161, 31))
        self.passLine.setObjectName("passLine")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(36, 40, 61, 16))
        self.userLabel.setObjectName("userLabel")
        self.passLabel = QtWidgets.QLabel(self.centralwidget)
        self.passLabel.setGeometry(QtCore.QRect(36, 90, 61, 16))
        self.passLabel.setObjectName("passLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(130, 160, 111, 31))
        self.loginButton.setObjectName("loginButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 352, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.loginButton.clicked.connect(self.login)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def login(self):
        logacc = Account()
        logacc.setUsername(self.userLine.text())
        logacc.setPassword(self.passLine.text())
        loginProcess(self,logacc)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.userLabel.setText(_translate("MainWindow", "Username:"))
        self.passLabel.setText(_translate("MainWindow", "Password:"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

