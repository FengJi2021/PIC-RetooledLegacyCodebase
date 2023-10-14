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

class Ui_NeuralNetwork(object):
    def setupUi(self, NeuralNetwork):
        NeuralNetwork.setObjectName(_fromUtf8("NeuralNetwork"))
        NeuralNetwork.resize(1251, 701)
        self.XIANSHI = QtGui.QPushButton(NeuralNetwork)
        self.XIANSHI.setGeometry(QtCore.QRect(450, 50, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.XIANSHI.setFont(font)
        self.XIANSHI.setObjectName(_fromUtf8("XIANSHI"))
        self.SHUJUBIAO = QtGui.QTableWidget(NeuralNetwork)
        self.SHUJUBIAO.setGeometry(QtCore.QRect(50, 120, 561, 521))
        self.SHUJUBIAO.setObjectName(_fromUtf8("SHUJUBIAO"))
        self.SHUJUBIAO.setColumnCount(0)
        self.SHUJUBIAO.setRowCount(0)
        self.label = QtGui.QLabel(NeuralNetwork)
        self.label.setGeometry(QtCore.QRect(50, 80, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(NeuralNetwork)
        self.label_3.setGeometry(QtCore.QRect(660, 80, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.JIEGUO = QtGui.QTableWidget(NeuralNetwork)
        self.JIEGUO.setGeometry(QtCore.QRect(660, 120, 561, 521))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.JIEGUO.setFont(font)
        self.JIEGUO.setObjectName(_fromUtf8("JIEGUO"))
        self.JIEGUO.setColumnCount(0)
        self.JIEGUO.setRowCount(0)
        self.XIANSHI_2 = QtGui.QPushButton(NeuralNetwork)
        self.XIANSHI_2.setGeometry(QtCore.QRect(1070, 50, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.XIANSHI_2.setFont(font)
        self.XIANSHI_2.setObjectName(_fromUtf8("XIANSHI_2"))
        self.line = QtGui.QFrame(NeuralNetwork)
        self.line.setGeometry(QtCore.QRect(630, 120, 20, 521))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(NeuralNetwork)
        QtCore.QMetaObject.connectSlotsByName(NeuralNetwork)

    def retranslateUi(self, NeuralNetwork):
        NeuralNetwork.setWindowTitle(_translate("NeuralNetwork", "Form", None))
        self.XIANSHI.setText(_translate("NeuralNetwork", "显示3D图片", None))
        self.label.setText(_translate("NeuralNetwork", "切削力数据表格", None))
        self.label_3.setText(_translate("NeuralNetwork", "神经网络学习结果", None))
        self.XIANSHI_2.setText(_translate("NeuralNetwork", "开始学习", None))

