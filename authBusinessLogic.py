
import sqlite3 as sq
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 


class Account:
    def setUsername(self,uname):
        self.username = uname
    def setPassword(self,pword):
        self.password = pword
    def setlName(self,lname):
        self.lname = lname
    def setfName(self,fname):
        self.fname = fname
    def setid(self,id):
        self.acccountid = id