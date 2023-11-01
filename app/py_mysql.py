# coding: utf-8
'''
Created on 2018/2/17

@author: Administrator
'''
import pymysql

class py_mysql_client():
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
            self.conn = pymysql.connect(**def_config)
            print ('Connected to MySQL<br />')
        except:
            print ('ERROR connecting to MySQL<br />')
            
    def executeSql(self, sql_str):
        cursor = self.conn.cursor()
        cursor.execute(sql_str)
#         if sql_str.upper().find('SELECT') != -1:
#             data = cursor.fetchall()
#             return data
#         else:
#             return "ok..."
        
        data = cursor.fetchall()
        self.conn.commit()    
        return data    
    
if __name__ == "__main__":
    mysql_client = py_mysql_client()
     
    sql_str = "select * from users" # where code='1'"
#     sql_str = "delete from students where code='005'"
    print (mysql_client.executeSql(sql_str))
    
    
