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


class Ui_Machinetoolrealtime(object):
    def setupUi(self, Machinetoolrealtime):
        Machinetoolrealtime.setObjectName(_fromUtf8("Machinetoolrealtime"))
        Machinetoolrealtime.resize(740, 598)
        self.label = QtGui.QLabel(Machinetoolrealtime)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.XUHAO = QtGui.QLineEdit(Machinetoolrealtime)
        self.XUHAO.setGeometry(QtCore.QRect(150, 40, 171, 41))
        self.XUHAO.setObjectName(_fromUtf8("XUHAO"))
        self.CHAXUN = QtGui.QPushButton(Machinetoolrealtime)
        self.CHAXUN.setGeometry(QtCore.QRect(360, 40, 93, 41))
        self.CHAXUN.setObjectName(_fromUtf8("CHAXUN"))
        self.SHOULISHUJU = QtGui.QTableWidget(Machinetoolrealtime)
        self.SHOULISHUJU.setGeometry(QtCore.QRect(40, 180, 661, 381))
        self.SHOULISHUJU.setObjectName(_fromUtf8("SHOULISHUJU"))
        self.SHOULISHUJU.setColumnCount(0)
        self.SHOULISHUJU.setRowCount(0)
        self.label_2 = QtGui.QLabel(Machinetoolrealtime)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Machinetoolrealtime)
        QtCore.QMetaObject.connectSlotsByName(Machinetoolrealtime)

    def retranslateUi(self, Machinetoolrealtime):
        Machinetoolrealtime.setWindowTitle(
            _translate("Machinetoolrealtime", "Form", None)
        )
        self.label.setText(_translate("Machinetoolrealtime", "机床序号", None))
        self.CHAXUN.setText(_translate("Machinetoolrealtime", "查询", None))
        self.label_2.setText(
            _translate("Machinetoolrealtime", "机床三轴受力数据表", None)
        )
