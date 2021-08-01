#coding: utf-8
'''
Created on 2018/3/29

@author: Administrator
'''
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtSql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import py_mysql
import qt_mysql
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from frmlogin import Ui_frmlogin
from mainform import Ui_MainWindow
from userinfo import Ui_Form
from machinetoolstatic import Ui_machinetoolstatic
from machinetoolupdate import Ui_machinetoolupdate
from CraftandprocessData import Ui_productcraftinfo
from machinetoolrealstate import Ui_Machinetoolrealtime
from NeuralNetworkUi import Ui_NeuralNetwork
from productpicture import Ui_Design

class start_main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workspace = QWorkspace()
        self.setCentralWidget(self.workspace) 
        
#         self.userinfo = start_userinfo()
# menu related app.
        self.ui.act_userinfo.triggered.connect(self.showUserinfo)
        self.ui.getMTstaticinfo.triggered.connect(self.showgetMTstaticinfo)
        self.ui.updateMTstaticinfo.triggered.connect(self.showupdateMTstaticinfo)
        self.ui.productcraft.triggered.connect(self.showcraftprocessdata)
        self.ui.machinetoolrealtime.triggered.connect(self.showrealtimestate)
        self.ui.HUATU.triggered.connect(self.showmatplotdata)
        self.ui.productdesign.triggered.connect(self.showproductpicture)
        self.ui.NeuralnetworkVisual.triggered.connect(self.showNeuralnetworkVisual)
        
    def showUserinfo(self):
        self.userinfo = start_userinfo()
        self.workspace.addWindow(self.userinfo)
        self.userinfo.show()
        
    def showgetMTstaticinfo(self):
        self.getMTstaticinfo = start_getMTstaticinfo()
        self.workspace.addWindow(self.getMTstaticinfo)
        self.getMTstaticinfo.show()
    
    def showupdateMTstaticinfo(self):
        self.updateMTstaticinfo = start_updateMTstaticinfo()
        self.workspace.addWindow(self.updateMTstaticinfo)
        self.updateMTstaticinfo.show()
    
    def showcraftprocessdata(self):
        self.craftprocessdata = start_craftprocessdata()
        self.workspace.addWindow(self.craftprocessdata)
        self.craftprocessdata.show()
     
    def showrealtimestate(self):
        self.realtimestate = start_realtimestate()
        self.workspace.addWindow(self.realtimestate)
        self.realtimestate.show()    
        
    def showmatplotdata(self):
        self.matplotdata = start_matplotdata()
        self.workspace.addWindow(self.matplotdata)
        self.matplotdata.show()
      
    def showproductpicture(self):
        self.productpic = start_productpicture()
        self.workspace.addWindow(self.productpic)
        self.productpic.show()
        
    def showNeuralnetworkVisual(self):
        self.NeuralnetworkVisual = start_NeuralnetworkVisual()
        self.workspace.addWindow(self.NeuralnetworkVisual)
        self.NeuralnetworkVisual.show()
        
class start_login(QtGui.QWidget): 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_frmlogin()
        self.ui.setupUi(self)
        self.ui.txtUser.setFocus()
        self.ui.txtPwd.setEchoMode(QLineEdit.Password)
        
        QtCore.QObject.connect(self.ui.btLogin, QtCore.SIGNAL("clicked()"), self.login)
        QtCore.QObject.connect(self.ui.btExit, QtCore.SIGNAL("clicked()"), self.close)

    def login(self):
        usr = self.ui.txtUser.text()
        pwd = self.ui.txtPwd.text()
        #默认的用户列表是userinfo
        sql_str = "select * from userinfo where userid='" + usr + "' and pwd='" +  pwd + "'"
        data = mysql_client.executeSql(sql_str)
        print (data)
        if len(data) == 0:
            print ("user id or password is wrong")
        else:
            myapp1.show()  
            self.close()  
        
class start_userinfo(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
                
        QtCore.QObject.connect(self.ui.CHAXUN, QtCore.SIGNAL("clicked()"), self.getData)
        QtCore.QObject.connect(self.ui.GENGXIN, QtCore.SIGNAL("clicked()"), self.insertData)
        QtCore.QObject.connect(self.ui.SHANCHU, QtCore.SIGNAL("clicked()"), self.deleteData)
        #initial my table
        self.ui.TABLE.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.ui.TABLE.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.ui.TABLE.setColumnCount(3)
        self.ui.TABLE.setHorizontalHeaderLabels(["用户ID","用户密码","用户名称"])
        self.ui.TABLE.setColumnWidth(0,250)
        self.ui.TABLE.setColumnWidth(1,250)
        self.ui.TABLE.setColumnWidth(2,250)
 
    def getData(self):  
        APPROVE = self.ui.YONGHUID.text()
        if APPROVE == str("最高权限") :   #hightest autority  
            sql_str = "select * from userinfo "
        else :
            sql_str = "select * from userinfo where userid='" + str(APPROVE) + "'"
            print(sql_str)
            
        datas = mysql_client.executeSql(sql_str)
        print(datas)
        rownumber = len(datas)
        self.ui.TABLE.setRowCount(rownumber)
        for i in range(0,rownumber) :
            self.ui.TABLE.setItem(i,0,QTableWidgetItem(str(datas[i][0])))
            self.ui.TABLE.setItem(i,1,QTableWidgetItem(str(datas[i][1])))
            self.ui.TABLE.setItem(i,2,QTableWidgetItem(str(datas[i][2])))

         
         
    def insertData(self):
        newid = self.ui.YONGHUID.text()
        newname = self.ui.XINID.text()
        newpwd = self.ui.XINMIMA.text()
        sql_str = "insert into userinfo  values ('" + newid + "','" + newpwd + "','" + newname + "')"
        print(sql_str)
        mysql_client.executeSql(sql_str)
        
    def deleteData(self):

        CONFIRM = "Confirm"
        CANCEL = 'Cancel'
        message = QtGui.QMessageBox(self)
        message.setText('Confirm to delete the record?')
        message.setWindowTitle('Attention...')
        message.setIcon(QtGui.QMessageBox.Question)
        message.addButton(CONFIRM, QtGui.QMessageBox.AcceptRole)
        message.addButton(CANCEL, QtGui.QMessageBox.RejectRole)
        message.exec_()
        response = message.clickedButton().text()
            # save file
        if response == CONFIRM and self.ui.YONGHUID.text() == "最高权限":
            print ("delete...")
            id = self.ui.XINID.text()
            sql_str = "delete from userinfo where name='" + str(id) + "'"
            print (sql_str)
            mysql_client.executeSql(sql_str)

class start_getMTstaticinfo(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_machinetoolstatic()
        self.ui.setupUi(self)
        
        self.ui.xuhao.setFocus()
        
        QtCore.QObject.connect(self.ui.chaxun, QtCore.SIGNAL("clicked()"), self.getData)

    def getData(self):
        id = self.ui.xuhao.text()
        sql_str = "select * from machinetool where id=" +str(id)
        data = mysql_client.executeSql(sql_str)
        print(data)
        self.ui.MINGC.setText(data[0][1])
        self.ui.GONGLV.setText(str(data[0][2]))
        self.ui.ZHUANGSU.setText(str(data[0][3]))
        self.ui.XFW.setText(str(data[0][4]))
        self.ui.YFW.setText(str(data[0][5]))
        self.ui.ZFW.setText(str(data[0][6]))
        self.ui.XSD.setText(str(data[0][7]))
        self.ui.YSD.setText(str(data[0][8]))
        self.ui.ZSD.setText(str(data[0][9]))
        self.ui.XITONG.setText(str(data[0][11]))
        self.ui.GZSJ.setText(str(data[0][12]))
        self.ui.BJCS.setText(str(data[0][13]))
    #cutting force reading data
        f =open('C:\\Users\\admin\\Desktop\\abschlussproject\\getforcetest.txt',mode='r')
        for each_line in f :
            (mytime,FX,FY,FZ) = each_line.split('\t',3)
            print(mytime,FX,FY,FZ)
            FZ =FZ[:-1]
            mysql_client.executeSql("INSERT INTO realtimestate VALUES ('" + mytime +"','1','" + FX +"','" + FY + "','" + FZ + "')")
            print(mytime,FX,FY,FZ)
    
class start_updateMTstaticinfo(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_machinetoolupdate()
        self.ui.setupUi(self)
        
        self.ui.xuhao.setFocus()    
        QtCore.QObject.connect(self.ui.gengxin, QtCore.SIGNAL("clicked()"), self.updateDate)
      
    def updateDate(self):
        id = self.ui.xuhao.text()
        #如果没有输入则返回空str
        list =[self.ui.MINGC.text(),self.ui.GONGLV.text(),self.ui.ZHUANGSU.text(),self.ui.XFW.text(),self.ui.YFW.text(),self.ui.ZFW.text(),self.ui.XSD.text(),self.ui.YSD.text(),self.ui.ZSD.text(),self.ui.XITONG.text(),self.ui.GZSJ.text(),self.ui.BJCS.text()]  
        sql_str1 = "UPDATE machinetool SET MTname ='" + str(list[0]) + "' WHERE id= '" + str(id)+"'"
        sql_str2 = "UPDATE machinetool SET MAPR ='" + str(list[1]) + "' WHERE id= '" + str(id)+"'"
        print("UPDATE machinetool SET MAPR =" + str(list[1]) + " WHERE id= '" + str(id)+"'")
        sql_str3 = "UPDATE machinetool SET RPM ='" + str(list[2]) + "' WHERE id= '" + str(id)+"'"
        sql_str4 = "UPDATE machinetool SET Xrange ='" + str(list[3]) + "' WHERE id= '" + str(id)+"'"
        sql_str5 = "UPDATE machinetool SET Yrange ='" + str(list[4]) + "' WHERE id= '" + str(id)+"'"
        sql_str6 = "UPDATE machinetool SET Zrange ='" + str(list[5]) + "' WHERE id= '" + str(id)+"'"
        sql_str7 = "UPDATE machinetool SET XFeedspeed ='" + str(list[6]) + "' WHERE id= '" + str(id)+"'"
        sql_str8 = "UPDATE machinetool SET YFeedspeed ='" + str(list[7]) + "' WHERE id= '" + str(id)+"'"
        sql_str9 = "UPDATE machinetool SET ZFeedspeed ='" + str(list[8]) + "' WHERE id= '" + str(id)+"'"
        sql_str10 = "UPDATE machinetool SET Controlsys ='" + str(list[9]) + "' WHERE id= '" + str(id)+"'"
        sql_str11 = "UPDATE machinetool SET Workinghour ='" + str(list[10]) + "' WHERE id= '" + str(id)+"'"
        sql_str12 = "UPDATE machinetool SET Alarmnumber ='" + str(list[11]) + "' WHERE id= '" + str(id)+"'"
        if list[0] == "" or list[1] ==""or list[2] ==""or list[3] ==""or list[4] ==""or list[5] ==""or list[6] ==""or list[7] ==""or list[8] ==""or list[9] ==""or list[10] ==""or list[11] =="":
            self.ui.tishi.setText('需要完整的表格输入')
             
        else :
            mysql_client.executeSql(sql_str1)
            mysql_client.executeSql(sql_str2)
            mysql_client.executeSql(sql_str3)
            mysql_client.executeSql(sql_str4)
            mysql_client.executeSql(sql_str5)
            mysql_client.executeSql(sql_str6)
            mysql_client.executeSql(sql_str7)
            mysql_client.executeSql(sql_str8)
            mysql_client.executeSql(sql_str9)
            mysql_client.executeSql(sql_str10)
            mysql_client.executeSql(sql_str11)
            mysql_client.executeSql(sql_str12) 
            self.ui.tishi.setText('完成机床ID为'+str(id)+'的表格更新')
        resultback = mysql_client.executeSql(sql_str1)
           
class start_craftprocessdata(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_productcraftinfo()
        self.ui.setupUi(self) 
        QtCore.QObject.connect(self.ui.CHAXUN, QtCore.SIGNAL("clicked()"), self.getData)
        QtCore.QObject.connect(self.ui.GONGYILURU, QtCore.SIGNAL("clicked()"), self.insertcraftData)
        QtCore.QObject.connect(self.ui.LURU, QtCore.SIGNAL("clicked()"), self.insertprocessData) 
        self.ui.GONGYIID.setPlaceholderText("工序号"). #production serie nummer 
        self.ui.GONGXUHAO.setPlaceholderText("工艺卡号") #production card nummer
        self.ui.NEIRONG.setPlaceholderText("工序内容") #production content
        self.ui.JICHUANG.setPlaceholderText("加工设备")#machine
         
    def getData(self):
        id = self.ui.LJID.text()
        sql_str = "select * from craftdata where craftid=" +str(id)
        data = mysql_client.executeSql(sql_str)
        print(data)
        self.ui.MINGCHENG.setText(data[0][4])
        self.ui.JINGZHONG.setText(data[0][5])
        self.ui.TUHAO.setText(data[0][3])
        self.ui.JIANSHU.setText(data[0][6])
        self.ui.PAIHAO.setText(data[0][2])
        sql_str2 = "select * from processdata where craftid="+str(id)
        data4process = mysql_client.executeSql(sql_str2)
        self.ui.GONGXU.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.ui.GONGXU.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.GONGXU.setRowCount(Rownumber)
        self.ui.GONGXU.setColumnCount(4)
        self.ui.GONGXU.setHorizontalHeaderLabels(["工序号","工序内容","工艺卡编号","加工设备"]) #production serie nummer,content,machine
        self.ui.GONGXU.setColumnWidth(1,450)
        self.ui.GONGXU.setColumnWidth(2,90)
        self.ui.GONGXU.setColumnWidth(3,80)
        for i in range(0,Rownumber):
            row = i
            self.ui.GONGXU.setItem(row,0,QTableWidgetItem(str(data4process[i][2])))
            self.ui.GONGXU.setItem(row,1,QTableWidgetItem(str(data4process[i][1])))
            self.ui.GONGXU.setItem(row,2,QTableWidgetItem(str(data4process[i][0])))
            self.ui.GONGXU.setItem(row,3,QTableWidgetItem(str(data4process[i][3])))
        
    def insertcraftData(self):
        id = self.ui.LJID.text()
        blankcategory = self.ui.MINGCHENG.text()
        materialname =self.ui.PAIHAO.text()
        cadid = self.ui.TUHAO.text()
        craftname = self.ui.MINGCHENG.text()
        blankweight = self.ui.JINGZHONG.text()
        blank4howmany = self.ui.JIANSHU.text()
        sql_str = "INSERT INTO craftdata VALUES ('" + id + "','" + blankcategory + "','" + materialname + "','" + cadid + "','" + craftname + "','" + blankweight + "','" + blank4howmany + "')"
        mysql_client.executeSql(sql_str)
        
    def insertprocessData(self):
        craftid = self.ui.GONGYIID.text()
        content = self.ui.NEIRONG.text()
        serialnumber = self.ui.GONGXUHAO.text()
        MTinfo = self.ui.JICHUANG.text()
        sql_str = "INSERT INTO processdata VALUES ('" + craftid + "','" + content + "','" + serialnumber + "','" + MTinfo + "')"
        mysql_client.executeSql(sql_str)

class start_realtimestate(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Machinetoolrealtime()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.CHAXUN, QtCore.SIGNAL("clicked()"), self.getData)
    def getData(self):
        id = self.ui.XUHAO.text()
        sql_str = "select * from realtimestate where MTid=" +str(id)
        data = mysql_client.executeSql(sql_str)
        Rownumber = len(data)
        print(Rownumber)
        self.ui.SHOULISHUJU.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.ui.SHOULISHUJU.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.SHOULISHUJU.setRowCount(Rownumber)
        self.ui.SHOULISHUJU.setColumnCount(4)
        self.ui.SHOULISHUJU.setHorizontalHeaderLabels(["时间(S)","Fx受力(N)","Fy受力(N)","Fz受力(N)"]) #time,force-x,y,z
        self.ui.SHOULISHUJU.setColumnWidth(1,150)
        self.ui.SHOULISHUJU.setColumnWidth(2,150)
        self.ui.SHOULISHUJU.setColumnWidth(3,150)
        for i in range(0,Rownumber):
            row = i
            self.ui.SHOULISHUJU.setItem(row,0,QTableWidgetItem(str(data[i][0])))
            self.ui.SHOULISHUJU.setItem(row,1,QTableWidgetItem(str(data[i][2])))
            self.ui.SHOULISHUJU.setItem(row,2,QTableWidgetItem(str(data[i][3])))
            self.ui.SHOULISHUJU.setItem(row,3,QTableWidgetItem(str(data[i][4])))
    
class start_matplotdata(QtGui.QWidget):  
      def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        figure = plt.gcf() #current figure
        self.canvas = figureCanvas(figure)
        sql_str = "select * from realtimestate where MTid= 1 " 
        data = mysql_client.executeSql(sql_str)
        listnumber = len(data)
        print(listnumber)
        time =[]
        FX =[]
        FY =[]
        FZ =[]
        for i in range(0,listnumber) :
            time.append(data[i][0])
            FX.append(data[i][2])
            FY.append(data[i][3])
            FZ.append(data[i][4])
        
        L1, = plt.plot(time,FX)
        L2, = plt.plot(time,FY)
        L3, = plt.plot(time,FZ)
        plt.legend(handles=[L1,L2,L3,],labels=["FX","FY","FZ"],loc="best")
        plt.title('FORCE MAP')
        plt.xlabel('Time(S)')
        plt.ylabel('Force(N)')
        self.canvas.draw()
        layout = QHBoxLayout(self)
        layout.addWidget(self.canvas)   

class start_productpicture(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Design()
        self.ui.setupUi(self)
        self.ui.GONGYIHAO.setPlaceholderText("请输入工艺编号"). #production serie nummer
        self.ui.GONGXUHAO.setPlaceholderText("请输入工序编号")
        QtCore.QObject.connect(self.ui.CHAXUN, QtCore.SIGNAL("clicked()"), self.getData)

    def getData(self):
        craftnumber = self.ui.GONGYIHAO.text()
        processnumber = self.ui.GONGXUHAO.text()
        sql_str = "select * from craftandcaddata where craftnumber=" +str(craftnumber) + " and processnumber= " + str(processnumber)
        print(sql_str)
        result = mysql_client.executeSql(sql_str)
        print(result)
        serial = result[0][1]
        sql_str = "select * from caddata where serial=" +str(serial)
        result = mysql_client.executeSql(sql_str)
        Adress = result[0][2]
        print(Adress)
        png=QtGui.QPixmap(str(Adress))  
        self.ui.TUPIAN.setPixmap(png)
 
class start_NeuralnetworkVisual(QtGui.QWidget): 
        def __init__(self,parent=None):
            QtGui.QWidget.__init__(self, parent)
            self.ui = Ui_NeuralNetwork()
            self.ui.setupUi(self)
            QtCore.QObject.connect(self.ui.XIANSHI, QtCore.SIGNAL("clicked()"), self.showVisual)
            QtCore.QObject.connect(self.ui.XIANSHI_2, QtCore.SIGNAL("clicked()"), self.showResult)
            samplesize = 20
            self.ui.SHUJUBIAO.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.ui.SHUJUBIAO.setSelectionBehavior(QAbstractItemView.SelectRows)              
            self.ui.SHUJUBIAO.setRowCount(samplesize**3)
            self.ui.SHUJUBIAO.setColumnCount(4)
            self.ui.SHUJUBIAO.setHorizontalHeaderLabels(["Fx受力(N)","主轴转速(m/min)","进给速度(mm/s)","吃刀量(mm)"]) #force,main-speed,feedspeed,cuttingdepth
            self.ui.SHUJUBIAO.setColumnWidth(1,130)
            self.ui.SHUJUBIAO.setColumnWidth(2,130)
            self.ui.SHUJUBIAO.setColumnWidth(3,130)
            #default data         
            x1_data = np.linspace(1, 60,samplesize , dtype=np.float32)   # x data
            x2_data = np.linspace(0.001,0.01,samplesize,dtype=np.float32)
            x3_data = np.linspace(2,3,samplesize,dtype=np.float32)
            x1_data,x2_data = np.meshgrid(x1_data,x2_data)
            x1_data,ignoreme = np.meshgrid(x1_data.flatten(),x3_data)
            x2_data,x3_data = np.meshgrid(x2_data.flatten(),x3_data)
            x1_data =x1_data.flatten();x2_data = x2_data.flatten();x3_data = x3_data.flatten()
            print(x1_data,x1_data.shape)
            Func = lambda :np.exp(np.log(248.945) + 0.135*np.log(x1_data) + 0.147*np.log(x2_data) + 0.62*np.log(x3_data))
            Fx = Func()
            rownumber = samplesize**3
            for i in range(0,rownumber):
                row = i
                self.ui.SHUJUBIAO.setItem(row,0,QTableWidgetItem(str(Fx[i])))
                self.ui.SHUJUBIAO.setItem(row,1,QTableWidgetItem(str(x1_data[i])))
                self.ui.SHUJUBIAO.setItem(row,2,QTableWidgetItem(str(x2_data[i])))
                self.ui.SHUJUBIAO.setItem(row,3,QTableWidgetItem(str(x3_data[i])))
             
        def showVisual(self):           
            LR = 0.005
            REAL_PARAMS = [0.135, 0.147]
            x1_data = np.linspace(1, 60, 20, dtype=np.float32)   # x data
            x2_data = np.linspace(0.001,0.01,20,dtype=np.float32)
            y_fun = lambda a, b: (np.log(248.945) + a*np.log(x1_data) + b*np.log(x2_data) + 0.62*np.log(2.)) #c的值默认是0.62
            tf_y_fun = lambda a, b: (tf.log(248.945) + a*tf.log(x1_data) + b*tf.log(x2_data) + 0.62*tf.log(2.))
            noise = np.random.randn(20)/10
            y = y_fun(*REAL_PARAMS)    +noise   # target
            # tensorflow graph

            def NeuralWorking(INITME):
                INIT_PARAMS = [[ 5,-10],
                           [-10, 2],
                           [10,-10],
                           [7.5,7.5],
                           [2.5,-4],
                           [-10,10],
                           [-10,-10],
                           [-10,2.5]][INITME]
                a, b = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
                pred = tf_y_fun(a, b)
                mse = tf.reduce_mean(tf.square(y-pred))
                train_op = tf.train.GradientDescentOptimizer(LR).minimize(mse)
    
                a_list, b_list, cost_list = [], [], []
                with tf.Session() as sess:
                    sess.run(tf.global_variables_initializer())
                    for t in range(4001):
                        a_, b_, mse_ = sess.run([a, b, mse])
                        a_list.append(a_); b_list.append(b_); cost_list.append(mse_)
                        result, _ = sess.run([pred, train_op])  
                return a_ , b_,a_list, b_list, cost_list
            fig = plt.figure(2); ax = Axes3D(fig)
            a3D, b3D = np.meshgrid(np.linspace(-10, 10, 30), np.linspace(-10,10, 30))  # parameter space
            cost3D = np.array([np.mean(np.square(y_fun(a_, b_) - y)) for a_, b_ in zip(a3D.flatten(), b3D.flatten())]).reshape(a3D.shape)
            ax.plot_surface(a3D, b3D, cost3D, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'), alpha=0.5)
            ax.set_xlabel('a'); ax.set_ylabel('b')
            a_list = NeuralWorking(0)[2]; b_list = NeuralWorking(0)[3];cost_list = NeuralWorking(0)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='r')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='r', lw=3) 
            a_list = NeuralWorking(1)[2]; b_list = NeuralWorking(1)[3];cost_list = NeuralWorking(1)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='g')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='g', lw=3) 
            a_list = NeuralWorking(2)[2]; b_list = NeuralWorking(2)[3];cost_list = NeuralWorking(2)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='b')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='b', lw=3) 
            a_list = NeuralWorking(3)[2]; b_list = NeuralWorking(3)[3];cost_list = NeuralWorking(3)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='y')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='y', lw=3) 
            a_list = NeuralWorking(4)[2]; b_list = NeuralWorking(4)[3];cost_list = NeuralWorking(4)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='k')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='b', lw=3) 
            a_list = NeuralWorking(5)[2]; b_list = NeuralWorking(5)[3];cost_list = NeuralWorking(5)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='m')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='m', lw=3) 
            a_list = NeuralWorking(6)[2]; b_list = NeuralWorking(6)[3];cost_list = NeuralWorking(6)[4]
            ax.scatter(a_list[0], b_list[0], zs=cost_list[0], s=300, c='c')
            ax.plot(a_list,b_list, zs=cost_list, zdir='z', c='c', lw=3)                              
            plt.show()

        def showResult(self):
            #initial
            self.ui.JIEGUO.setEditTriggers(QAbstractItemView.NoEditTriggers) 
            self.ui.JIEGUO.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.ui.JIEGUO.setRowCount(5000)
            self.ui.JIEGUO.setColumnCount(5)
            self.ui.JIEGUO.setHorizontalHeaderLabels(["误差均方值","A的取值","B的取值","C的取值","D的取值"]) #varianze
            self.ui.JIEGUO.setColumnWidth(1,100)
            self.ui.JIEGUO.setColumnWidth(2,100)
            self.ui.JIEGUO.setColumnWidth(3,100)
            self.ui.JIEGUO.setColumnWidth(4,100)
            LR = 0.005
            REAL_PARAMS = [0.135, 0.147,0.62,2.3961]
            INIT_PARAMS = [[0.3,0.3,0.3,2.3],
                           [0.2,0.2,0.2,2.3961],
                           [0.1,0.1,0.5,2.39]][2]
            samplesize = 100
            x1_data = np.linspace(1, 60, samplesize, dtype=np.float32)   # x data
            x2_data = np.linspace(0.001,0.01,samplesize,dtype=np.float32)
            x3_data = np.linspace(2,3,samplesize,dtype=np.float32)
            y_fun = lambda a, b, c,d: d + a*np.log(x1_data) + b*np.log(x2_data) + c*np.log(x3_data)
            tf_y_fun = lambda a, b, c,d: d + a*tf.log(x1_data) + b*tf.log(x2_data) + c*tf.log(x3_data)
            noise = np.random.randn(samplesize)/10
            y = y_fun(*REAL_PARAMS) +noise     # target
            # tensorflow graph
            a, b, c,d = [tf.Variable(initial_value=p, dtype=tf.float32) for p in INIT_PARAMS]
            pred = tf_y_fun(a, b, c,d)
            mse = tf.reduce_mean(tf.square(y-pred))
            train_op = tf.train.AdamOptimizer(LR).minimize(mse)
            a_list, b_list,c_list,d_list, cost_list = [], [], [], [], []
            with tf.Session() as sess:
                sess.run(tf.global_variables_initializer())
                for t in range(5000):
                    a_, b_,c_,d_, mse_ = sess.run([a, b, c,d, mse])
                    #result to table
                    self.ui.JIEGUO.setItem(t,0,QTableWidgetItem(str(mse_)))
                    self.ui.JIEGUO.setItem(t,1,QTableWidgetItem(str(a_)))
                    self.ui.JIEGUO.setItem(t,2,QTableWidgetItem(str(b_)))
                    self.ui.JIEGUO.setItem(t,3,QTableWidgetItem(str(c_)))
                    self.ui.JIEGUO.setItem(t,4,QTableWidgetItem(str(d_)))
                    a_list.append(a_); b_list.append(b_); c_list.append(c_); d_list.append(d_);cost_list.append(mse_)
                    result, _ = sess.run([pred, train_op])  
            
if __name__ == "__main__":
    print (sys.argv)
    app = QtGui.QApplication(sys.argv)
    mysql_client = py_mysql.py_mysql_client()
    
    myapp = start_login()
    myapp1 = start_main()
    
    myapp.show()
    sys.exit(app.exec_())
