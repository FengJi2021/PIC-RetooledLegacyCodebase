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


class Ui_machinetoolstatic(object):
    def setupUi(self, machinetoolstatic):
        machinetoolstatic.setObjectName(_fromUtf8("machinetoolstatic"))
        machinetoolstatic.resize(741, 599)
        font = QtGui.QFont()
        font.setPointSize(11)
        machinetoolstatic.setFont(font)
        self.xuhao = QtGui.QLineEdit(machinetoolstatic)
        self.xuhao.setGeometry(QtCore.QRect(150, 40, 171, 41))
        self.xuhao.setObjectName(_fromUtf8("xuhao"))
        self.label = QtGui.QLabel(machinetoolstatic)
        self.label.setGeometry(QtCore.QRect(40, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(machinetoolstatic)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(machinetoolstatic)
        self.label_3.setGeometry(QtCore.QRect(40, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(machinetoolstatic)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 181, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(machinetoolstatic)
        self.label_5.setGeometry(QtCore.QRect(80, 390, 71, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(machinetoolstatic)
        self.label_6.setGeometry(QtCore.QRect(80, 440, 71, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(machinetoolstatic)
        self.label_7.setGeometry(QtCore.QRect(80, 490, 71, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(machinetoolstatic)
        self.label_8.setGeometry(QtCore.QRect(390, 390, 91, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(machinetoolstatic)
        self.label_9.setGeometry(QtCore.QRect(390, 440, 91, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(machinetoolstatic)
        self.label_10.setGeometry(QtCore.QRect(390, 490, 91, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(machinetoolstatic)
        self.label_11.setGeometry(QtCore.QRect(450, 160, 81, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(machinetoolstatic)
        self.label_12.setGeometry(QtCore.QRect(450, 210, 81, 31))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(machinetoolstatic)
        self.label_13.setGeometry(QtCore.QRect(450, 100, 81, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(machinetoolstatic)
        self.label_14.setGeometry(QtCore.QRect(450, 270, 81, 31))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.chaxun = QtGui.QPushButton(machinetoolstatic)
        self.chaxun.setGeometry(QtCore.QRect(330, 40, 93, 41))
        self.chaxun.setObjectName(_fromUtf8("chaxun"))
        self.MINGC = QtGui.QLineEdit(machinetoolstatic)
        self.MINGC.setGeometry(QtCore.QRect(150, 100, 271, 51))
        self.MINGC.setObjectName(_fromUtf8("MINGC"))
        self.GONGLV = QtGui.QLineEdit(machinetoolstatic)
        self.GONGLV.setGeometry(QtCore.QRect(40, 220, 341, 41))
        self.GONGLV.setObjectName(_fromUtf8("GONGLV"))
        self.ZHUANGSU = QtGui.QLineEdit(machinetoolstatic)
        self.ZHUANGSU.setGeometry(QtCore.QRect(40, 320, 341, 41))
        self.ZHUANGSU.setObjectName(_fromUtf8("ZHUANGSU"))
        self.XFW = QtGui.QLineEdit(machinetoolstatic)
        self.XFW.setGeometry(QtCore.QRect(140, 380, 211, 41))
        self.XFW.setObjectName(_fromUtf8("XFW"))
        self.YFW = QtGui.QLineEdit(machinetoolstatic)
        self.YFW.setGeometry(QtCore.QRect(140, 430, 211, 41))
        self.YFW.setObjectName(_fromUtf8("YFW"))
        self.ZFW = QtGui.QLineEdit(machinetoolstatic)
        self.ZFW.setGeometry(QtCore.QRect(140, 480, 211, 41))
        self.ZFW.setObjectName(_fromUtf8("ZFW"))
        self.XSD = QtGui.QLineEdit(machinetoolstatic)
        self.XSD.setGeometry(QtCore.QRect(480, 380, 211, 41))
        self.XSD.setObjectName(_fromUtf8("XSD"))
        self.YSD = QtGui.QLineEdit(machinetoolstatic)
        self.YSD.setGeometry(QtCore.QRect(480, 430, 211, 41))
        self.YSD.setObjectName(_fromUtf8("YSD"))
        self.ZSD = QtGui.QLineEdit(machinetoolstatic)
        self.ZSD.setGeometry(QtCore.QRect(480, 480, 211, 41))
        self.ZSD.setObjectName(_fromUtf8("ZSD"))
        self.ZHUANGTAI = QtGui.QLineEdit(machinetoolstatic)
        self.ZHUANGTAI.setGeometry(QtCore.QRect(530, 90, 181, 41))
        self.ZHUANGTAI.setObjectName(_fromUtf8("ZHUANGTAI"))
        self.GZSJ = QtGui.QLineEdit(machinetoolstatic)
        self.GZSJ.setGeometry(QtCore.QRect(530, 150, 181, 41))
        self.GZSJ.setObjectName(_fromUtf8("GZSJ"))
        self.BJCS = QtGui.QLineEdit(machinetoolstatic)
        self.BJCS.setGeometry(QtCore.QRect(530, 210, 181, 41))
        self.BJCS.setObjectName(_fromUtf8("BJCS"))
        self.XITONG = QtGui.QLineEdit(machinetoolstatic)
        self.XITONG.setGeometry(QtCore.QRect(530, 270, 181, 41))
        self.XITONG.setObjectName(_fromUtf8("XITONG"))

        self.retranslateUi(machinetoolstatic)
        QtCore.QMetaObject.connectSlotsByName(machinetoolstatic)

    def retranslateUi(self, machinetoolstatic):
        machinetoolstatic.setWindowTitle(
            _translate("machinetoolstatic", "Machinetoolstatic", None)
        )
        self.label.setText(_translate("machinetoolstatic", "机床序号", None))
        self.label_2.setText(_translate("machinetoolstatic", "机床名称", None))
        self.label_3.setText(_translate("machinetoolstatic", "机床最大功率", None))
        self.label_4.setText(_translate("machinetoolstatic", "机床最大转速", None))
        self.label_5.setText(_translate("machinetoolstatic", "X坐标", None))
        self.label_6.setText(_translate("machinetoolstatic", "Y坐标", None))
        self.label_7.setText(_translate("machinetoolstatic", "Z坐标", None))
        self.label_8.setText(_translate("machinetoolstatic", "X进给速度", None))
        self.label_9.setText(_translate("machinetoolstatic", "Y进给速度", None))
        self.label_10.setText(_translate("machinetoolstatic", "Z进给速度", None))
        self.label_11.setText(_translate("machinetoolstatic", "工作时间 ", None))
        self.label_12.setText(_translate("machinetoolstatic", "报警次数", None))
        self.label_13.setText(_translate("machinetoolstatic", "运行状况", None))
        self.label_14.setText(_translate("machinetoolstatic", "操作系统", None))
        self.chaxun.setText(_translate("machinetoolstatic", "查询", None))
