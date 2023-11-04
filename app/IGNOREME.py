# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mysoft.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)

except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1043, 778)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        self.menu_5 = QtGui.QMenu(self.menu_2)
        self.menu_5.setObjectName(_fromUtf8("menu_5"))
        self.menu_3 = QtGui.QMenu(self.menubar)
        self.menu_3.setObjectName(_fromUtf8("menu_3"))
        self.menu_4 = QtGui.QMenu(self.menubar)
        self.menu_4.setObjectName(_fromUtf8("menu_4"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.productstatic = QtGui.QAction(MainWindow)
        self.productstatic.setObjectName(_fromUtf8("productstatic"))
        self.productrealtime = QtGui.QAction(MainWindow)
        self.productrealtime.setObjectName(_fromUtf8("productrealtime"))
        self.productcraft = QtGui.QAction(MainWindow)
        self.productcraft.setObjectName(_fromUtf8("productcraft"))
        self.act_userinfo = QtGui.QAction(MainWindow)
        self.act_userinfo.setCheckable(False)
        self.act_userinfo.setObjectName(_fromUtf8("act_userinfo"))
        self.act_userpwd = QtGui.QAction(MainWindow)
        self.act_userpwd.setObjectName(_fromUtf8("act_userpwd"))
        self.machinetoolrealtime = QtGui.QAction(MainWindow)
        self.machinetoolrealtime.setObjectName(
            _fromUtf8("machinetoolrealtime")
        )
        self.productdesign = QtGui.QAction(MainWindow)
        self.productdesign.setObjectName(_fromUtf8("productdesign"))
        self.NeuralnetworkVisual = QtGui.QAction(MainWindow)
        self.NeuralnetworkVisual.setObjectName(
            _fromUtf8("NeuralnetworkVisual")
        )
        self.getMTstaticinfo = QtGui.QAction(MainWindow)
        self.getMTstaticinfo.setObjectName(_fromUtf8("getMTstaticinfo"))
        self.updateMTstaticinfo = QtGui.QAction(MainWindow)
        self.updateMTstaticinfo.setObjectName(_fromUtf8("updateMTstaticinfo"))
        self.menu.addAction(self.act_userinfo)
        self.menu.addAction(self.act_userpwd)
        self.menu_5.addAction(self.getMTstaticinfo)
        self.menu_5.addAction(self.updateMTstaticinfo)
        self.menu_2.addAction(self.menu_5.menuAction())
        self.menu_2.addAction(self.machinetoolrealtime)
        self.menu_3.addAction(self.productstatic)
        self.menu_3.addAction(self.productrealtime)
        self.menu_3.addAction(self.productcraft)
        self.menu_3.addAction(self.productdesign)
        self.menu_4.addAction(self.NeuralnetworkVisual)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menu.setTitle(_translate("MainWindow", "用户信息管理", None))
        self.menu_2.setTitle(_translate("MainWindow", "机床信息管理", None))
        self.menu_5.setTitle(_translate("MainWindow", "机床静态信息", None))
        self.menu_3.setTitle(_translate("MainWindow", "产品信息管理", None))
        self.menu_4.setTitle(_translate("MainWindow", "生产线", None))
        self.productstatic.setText(_translate("MainWindow", "产品静态信息", None))
        self.productrealtime.setText(_translate("MainWindow", "产品实时信息", None))
        self.productcraft.setText(_translate("MainWindow", "产品工艺信息", None))
        self.act_userinfo.setText(_translate("MainWindow", "用户信息管理", None))
        self.act_userpwd.setText(_translate("MainWindow", "用户密码管理", None))
        self.machinetoolrealtime.setText(
            _translate("MainWindow", "机床实时信息", None)
        )
        self.productdesign.setText(_translate("MainWindow", "机床设计信息", None))
        self.productline.setText(
            _translate("MainWNeuralnetworkVisual线工况", None)
        )
        self.getMTstaticinfo.setText(_translate("MainWindow", "查询", None))
        self.updateMTstaticinfo.setText(_translate("MainWindow", "更新", None))
