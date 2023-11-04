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


class Ui_productcraftinfo(object):
    def setupUi(self, productcraftinfo):
        productcraftinfo.setObjectName(_fromUtf8("productcraftinfo"))
        productcraftinfo.resize(841, 672)
        font = QtGui.QFont()
        font.setUnderline(False)
        productcraftinfo.setFont(font)
        self.label = QtGui.QLabel(productcraftinfo)
        self.label.setGeometry(QtCore.QRect(60, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.LJID = QtGui.QLineEdit(productcraftinfo)
        self.LJID.setGeometry(QtCore.QRect(140, 30, 221, 41))
        self.LJID.setObjectName(_fromUtf8("LJID"))
        self.label_2 = QtGui.QLabel(productcraftinfo)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(productcraftinfo)
        self.label_3.setGeometry(QtCore.QRect(490, 40, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(productcraftinfo)
        self.label_4.setGeometry(QtCore.QRect(490, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(productcraftinfo)
        self.label_5.setGeometry(QtCore.QRect(40, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(productcraftinfo)
        self.label_6.setGeometry(QtCore.QRect(490, 140, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(productcraftinfo)
        self.label_7.setGeometry(QtCore.QRect(40, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.GONGXU = QtGui.QTableWidget(productcraftinfo)
        self.GONGXU.setGeometry(QtCore.QRect(40, 240, 761, 321))
        self.GONGXU.setObjectName(_fromUtf8("GONGXU"))
        self.CHAXUN = QtGui.QPushButton(productcraftinfo)
        self.CHAXUN.setGeometry(QtCore.QRect(370, 30, 93, 41))
        self.CHAXUN.setObjectName(_fromUtf8("CHAXUN"))
        self.MINGCHENG = QtGui.QLineEdit(productcraftinfo)
        self.MINGCHENG.setGeometry(QtCore.QRect(140, 80, 221, 41))
        self.MINGCHENG.setObjectName(_fromUtf8("MINGCHENG"))
        self.JINGZHONG = QtGui.QLineEdit(productcraftinfo)
        self.JINGZHONG.setGeometry(QtCore.QRect(140, 130, 221, 41))
        self.JINGZHONG.setObjectName(_fromUtf8("JINGZHONG"))
        self.TUHAO = QtGui.QLineEdit(productcraftinfo)
        self.TUHAO.setGeometry(QtCore.QRect(580, 30, 221, 41))
        self.TUHAO.setObjectName(_fromUtf8("TUHAO"))
        self.JIANSHU = QtGui.QLineEdit(productcraftinfo)
        self.JIANSHU.setGeometry(QtCore.QRect(620, 80, 181, 41))
        self.JIANSHU.setObjectName(_fromUtf8("JIANSHU"))
        self.PAIHAO = QtGui.QLineEdit(productcraftinfo)
        self.PAIHAO.setGeometry(QtCore.QRect(580, 130, 221, 41))
        self.PAIHAO.setObjectName(_fromUtf8("PAIHAO"))
        self.GONGYIID = QtGui.QLineEdit(productcraftinfo)
        self.GONGYIID.setGeometry(QtCore.QRect(40, 580, 121, 41))
        self.GONGYIID.setObjectName(_fromUtf8("GONGYIID"))
        self.NEIRONG = QtGui.QLineEdit(productcraftinfo)
        self.NEIRONG.setGeometry(QtCore.QRect(300, 580, 371, 41))
        self.NEIRONG.setObjectName(_fromUtf8("NEIRONG"))
        self.GONGXUHAO = QtGui.QLineEdit(productcraftinfo)
        self.GONGXUHAO.setGeometry(QtCore.QRect(170, 580, 113, 41))
        self.GONGXUHAO.setObjectName(_fromUtf8("GONGXUHAO"))
        self.JICHUANG = QtGui.QLineEdit(productcraftinfo)
        self.JICHUANG.setGeometry(QtCore.QRect(690, 580, 113, 41))
        self.JICHUANG.setObjectName(_fromUtf8("JICHUANG"))
        self.LURU = QtGui.QPushButton(productcraftinfo)
        self.LURU.setGeometry(QtCore.QRect(690, 190, 111, 41))
        self.LURU.setObjectName(_fromUtf8("LURU"))
        self.GONGYILURU = QtGui.QPushButton(productcraftinfo)
        self.GONGYILURU.setGeometry(QtCore.QRect(370, 80, 93, 41))
        self.GONGYILURU.setObjectName(_fromUtf8("GONGYILURU"))

        self.retranslateUi(productcraftinfo)
        QtCore.QMetaObject.connectSlotsByName(productcraftinfo)
        productcraftinfo.setTabOrder(self.LJID, self.MINGCHENG)
        productcraftinfo.setTabOrder(self.MINGCHENG, self.JINGZHONG)
        productcraftinfo.setTabOrder(self.JINGZHONG, self.TUHAO)
        productcraftinfo.setTabOrder(self.TUHAO, self.JIANSHU)
        productcraftinfo.setTabOrder(self.JIANSHU, self.PAIHAO)
        productcraftinfo.setTabOrder(self.PAIHAO, self.GONGXU)
        productcraftinfo.setTabOrder(self.GONGXU, self.CHAXUN)

    def retranslateUi(self, productcraftinfo):
        productcraftinfo.setWindowTitle(
            _translate("productcraftinfo", "Form", None)
        )
        self.label.setText(_translate("productcraftinfo", "工艺ID", None))
        self.label_2.setText(_translate("productcraftinfo", "产品净重", None))
        self.label_3.setText(_translate("productcraftinfo", "零件图号", None))
        self.label_4.setText(_translate("productcraftinfo", "毛坯可制件数", None))
        self.label_5.setText(_translate("productcraftinfo", "工艺名称", None))
        self.label_6.setText(_translate("productcraftinfo", "材料牌号", None))
        self.label_7.setText(_translate("productcraftinfo", "零件工序表格", None))
        self.CHAXUN.setText(_translate("productcraftinfo", "查询", None))
        self.LURU.setText(_translate("productcraftinfo", "录入工序", None))
        self.GONGYILURU.setText(_translate("productcraftinfo", "录入工艺", None))
