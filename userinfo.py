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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(887, 632)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 70, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(460, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.YONGHUID = QtGui.QLineEdit(Form)
        self.YONGHUID.setGeometry(QtCore.QRect(190, 50, 231, 61))
        self.YONGHUID.setObjectName(_fromUtf8("YONGHUID"))
        self.XINID = QtGui.QLineEdit(Form)
        self.XINID.setGeometry(QtCore.QRect(190, 150, 231, 61))
        self.XINID.setObjectName(_fromUtf8("XINID"))
        self.XINMIMA = QtGui.QLineEdit(Form)
        self.XINMIMA.setGeometry(QtCore.QRect(600, 150, 231, 61))
        self.XINMIMA.setObjectName(_fromUtf8("XINMIMA"))
        self.TABLE = QtGui.QTableWidget(Form)
        self.TABLE.setGeometry(QtCore.QRect(60, 250, 771, 321))
        self.TABLE.setObjectName(_fromUtf8("TABLE"))
        self.TABLE.setColumnCount(0)
        self.TABLE.setRowCount(0)
        self.CHAXUN = QtGui.QPushButton(Form)
        self.CHAXUN.setGeometry(QtCore.QRect(460, 50, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CHAXUN.setFont(font)
        self.CHAXUN.setObjectName(_fromUtf8("CHAXUN"))
        self.GENGXIN = QtGui.QPushButton(Form)
        self.GENGXIN.setGeometry(QtCore.QRect(600, 50, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.GENGXIN.setFont(font)
        self.GENGXIN.setObjectName(_fromUtf8("GENGXIN"))
        self.SHANCHU = QtGui.QPushButton(Form)
        self.SHANCHU.setGeometry(QtCore.QRect(740, 50, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SHANCHU.setFont(font)
        self.SHANCHU.setObjectName(_fromUtf8("SHANCHU"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "用户ID", None))
        self.label_2.setText(_translate("Form", "用户名称", None))
        self.label_3.setText(_translate("Form", "用户密码", None))
        self.CHAXUN.setText(_translate("Form", "查询", None))
        self.GENGXIN.setText(_translate("Form", "更新", None))
        self.SHANCHU.setText(_translate("Form", "删除", None))

