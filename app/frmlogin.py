# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmlogin.ui'
#
# Created: Fri Mar 30 09:18:16 2018
#      by: PyQt4 UI code generator 4.11.3
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


class Ui_frmlogin(object):
    def setupUi(self, frmlogin):
        frmlogin.setObjectName(_fromUtf8("frmlogin"))
        frmlogin.resize(398, 273)
        self.btLogin = QtGui.QPushButton(frmlogin)
        self.btLogin.setGeometry(QtCore.QRect(53, 190, 101, 31))
        self.btLogin.setObjectName(_fromUtf8("btLogin"))
        self.label = QtGui.QLabel(frmlogin)
        self.label.setGeometry(QtCore.QRect(79, 60, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(frmlogin)
        self.label_2.setGeometry(QtCore.QRect(79, 120, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btExit = QtGui.QPushButton(frmlogin)
        self.btExit.setGeometry(QtCore.QRect(243, 190, 101, 31))
        self.btExit.setObjectName(_fromUtf8("btExit"))
        self.txtPwd = QtGui.QLineEdit(frmlogin)
        self.txtPwd.setGeometry(QtCore.QRect(149, 110, 141, 31))
        self.txtPwd.setObjectName(_fromUtf8("txtPwd"))
        self.txtUser = QtGui.QLineEdit(frmlogin)
        self.txtUser.setGeometry(QtCore.QRect(149, 50, 141, 31))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))

        self.retranslateUi(frmlogin)
        QtCore.QMetaObject.connectSlotsByName(frmlogin)

    def retranslateUi(self, frmlogin):
        frmlogin.setWindowTitle(_translate("frmlogin", "系统登录", None))
        self.btLogin.setText(_translate("frmlogin", "登录", None))
        self.label.setText(_translate("frmlogin", "用户名：", None))
        self.label_2.setText(_translate("frmlogin", "密  码：", None))
        self.btExit.setText(_translate("frmlogin", "取消", None))
