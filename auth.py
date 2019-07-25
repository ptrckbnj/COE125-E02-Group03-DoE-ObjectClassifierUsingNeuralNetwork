# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:28:48 2019

@author: derick
"""


import sqlite3 as sq
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 

def loginProcess(self,acc):
        accFound = False
        user = Account()
        accountBasis = Account()
        #userFile = open(r'userinfo.csv','r')
        
        
        user.setUsername(acc.username)
        user.setPassword(acc.password)
        
        if user.username.__len__() == 0 or user.password.__len__() == 0:
            mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            
            mess.setText("Cannot accept blank inputs")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()
        else:
            connection = sq.connect("users.db")
            con = connection.cursor()
            con.execute("SELECT accountid,fname,lname FROM accounts WHERE username = ? and password = ?",(user.username,user.password))
            userdata = con.fetchone()
            if userdata is None:
                 mess = QMessageBox()
                 mess.setIcon(QMessageBox.Critical)
                 mess.setText("You failed to login! Wrong Username/Password")
                 mess.setWindowTitle("Error")
                 mess.setStandardButtons(QMessageBox.Ok)
                 mess.exec()
               
            else:
                user.setUsername(acc.username)
                user.setPassword(acc.password)
                user.setid(userdata[0])
                user.setfName(userdata[1])
                user.setlName(userdata[2])
            
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Information)
                mess.setText("Hello " + user.fname +" "+ user.lname + "! You have successfully logged in.")
                mess.setWindowTitle("Successful Login")
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec()
                accFound = True
           
            """
            accountBasis = users[0]
            for rows in users:
                userInfo = fileLine.split(',')
                accountBasis.setUsername(userInfo[0])
                accountBasis.setPassword(userInfo[1])
                accountBasis.setName(userInfo[2])
          
                if user.username == accountBasis.username and user.password == accountBasis.password:
                    user.setName(accountBasis.name)
                    mess = lt.QMessageBox()
                    mess.setIcon(lt.QMessageBox.Information)
                    mess.setText("Hello " + user.name + "! You have successfully logged in.")
                    mess.setWindowTitle("Successful Login")
                    mess.setStandardButtons(lt.QMessageBox.Ok)
                    mess.exec()
                    self.userLine.clear()
                    self.passLine.clear()
                    accFound = True
                    break
                elif user.username == accountBasis.username and user.password != accountBasis.password:
                    mess = lt.QMessageBox()
                    mess.setIcon(lt.QMessageBox.Critical)
                    mess.setText("You failed to login! Wrong Password")
                    mess.setWindowTitle("Error")
                    mess.setStandardButtons(lt.QMessageBox.Ok)
                    mess.exec()
                    self.userLine.clear()
                    self.passLine.clear()
                    accFound = True
                    break
            userFile.close()
            
            if accFound == False:
                mess = lt.QMessageBox()
                mess.setIcon(lt.QMessageBox.Critical)
                mess.setText("Account does not exist")
                mess.setWindowTitle("Error")
                mess.setStandardButtons(lt.QMessageBox.Ok)
                mess.exec()
                self.userLine.clear()
                self.passLine.clear()
            """
            
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