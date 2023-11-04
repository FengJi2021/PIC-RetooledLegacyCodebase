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


class Ui_Design(object):
    def setupUi(self, Design):
        Design.setObjectName(_fromUtf8("Design"))
        Design.resize(1016, 825)
        self.label = QtGui.QLabel(Design)
        self.label.setGeometry(QtCore.QRect(50, 20, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.TUPIAN = QtGui.QLabel(Design)
        self.TUPIAN.setGeometry(QtCore.QRect(40, 110, 950, 700))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.TUPIAN.setFont(font)
        self.TUPIAN.setObjectName(_fromUtf8("TUPIAN"))
        self.GONGYIHAO = QtGui.QLineEdit(Design)
        self.GONGYIHAO.setGeometry(QtCore.QRect(50, 60, 181, 41))
        self.GONGYIHAO.setObjectName(_fromUtf8("GONGYIHAO"))
        self.CHAXUN = QtGui.QPushButton(Design)
        self.CHAXUN.setGeometry(QtCore.QRect(480, 60, 121, 41))
        self.CHAXUN.setObjectName(_fromUtf8("CHAXUN"))
        self.GONGXUHAO = QtGui.QLineEdit(Design)
        self.GONGXUHAO.setGeometry(QtCore.QRect(260, 60, 181, 41))
        self.GONGXUHAO.setObjectName(_fromUtf8("GONGXUHAO"))

        self.retranslateUi(Design)
        QtCore.QMetaObject.connectSlotsByName(Design)

    def retranslateUi(self, Design):
        Design.setWindowTitle(_translate("Design", "Form", None))
        self.label.setText(_translate("Design", "零件工艺和工序", None))
        self.TUPIAN.setText(_translate("Design", "图片显示", None))
        self.CHAXUN.setText(_translate("Design", "查询CAD", None))
