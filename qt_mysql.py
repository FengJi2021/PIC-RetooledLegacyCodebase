# coding: utf-8
'''
Created on 2018��4��1��

@author: Administrator
'''
from PyQt4.QtSql import *
from PyQt4.QtCore import *

class qt_mysql_client():
    def __init__(self, **config):
        try:
            if len(config) == 0:
                def_config = {
                  'host': "127.0.0.1",
                  'port': 3306,
                  'user': "root",
                  'passwd': "TonyStarK951753",
                  'charset':'utf8mb4',
                  'db': "myproject"
                  } 
# why is the following statement needed? any other way instead?                 
            QCoreApplication.addLibraryPath("C:\\Users\\admin\\Anaconda3\\Lib\\site-packages\\PyQt4\\plugins")
            self.db = QSqlDatabase.addDatabase("QMYSQL")
            self.db.setHostName(def_config['host'])
            self.db.setDatabaseName(def_config['db'])
            self.db.setUserName(def_config['user'])
            self.db.setPassword(def_config['passwd'])
            ok = self.db.open()
            if ok:
                print ('Connected1 to MySQL<br />')
            else:
                print ('ERROR1 connecting to MySQL<br />')
        except:
            print ('ERROR connecting to MySQL<br />')
            
if __name__ == "__main__":
    mysql_client = qt_mysql_client()          