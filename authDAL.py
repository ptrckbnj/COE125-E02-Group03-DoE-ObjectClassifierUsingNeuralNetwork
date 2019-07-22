
import sqlite3 as sq
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 

def loginProcess(self,acc):
        user = Account()
        value = False
        
        user.setUsername(acc.username)
        user.setPassword(acc.password)
        
        if user.username.__len__() == 0 or user.password.__len__() == 0:
            value = False
            '''  mess = QMessageBox()
            mess.setIcon(QMessageBox.Information)
            
            mess.setText("Cannot accept blank inputs")
            mess.setWindowTitle("Input error")
            mess.setStandardButtons(QMessageBox.Ok)
            mess.exec()'''
        else:
            connection = sq.connect("acc.db")
            con = connection.cursor()
            con.execute("SELECT accountid,fname,lname FROM accounts WHERE username = ? and password = ?",(user.username,user.password))
            userdata = con.fetchone()
            connection.close()
            if userdata is None:
                 '''
                 mess = QMessageBox()
                 mess.setIcon(QMessageBox.Critical)
                 mess.setText("You failed to login! Wrong Username/Password")
                 mess.setWindowTitle("Error")
                 mess.setStandardButtons(QMessageBox.Ok)
                 mess.exec()
                 '''
                 value = False
            else:
                user.setUsername(acc.username)
                user.setPassword(acc.password)
                user.setid(userdata[0])
                user.setfName(userdata[1])
                user.setlName(userdata[2])
                '''
                mess = QMessageBox()
                mess.setIcon(QMessageBox.Information)
                mess.setText("Hello " + user.fname +" "+ user.lname + "! You have successfully logged in.")
                mess.setWindowTitle("Successful Login")
                mess.setStandardButtons(QMessageBox.Ok)
                mess.exec()
                '''
                value = True
        return value
def registerAcc(self,acc):
    try:
        connection = sq.connect("acc.db")
        commands = '''INSERT INTO accounts (fname,lname,username,password) VALUES (?,?,?,?);'''
        cur = connection.cursor()
        cur.execute(commands,(acc.fname,acc.lname,acc.username,acc.password))
        #val =cur.lastrowid
        connection.commit()
        return True
    except:
        return False
