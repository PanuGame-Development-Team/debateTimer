# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.label1 = QtWidgets.QLabel(Form)
        self.label1.setGeometry(QtCore.QRect(60, 30, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.time1 = QtWidgets.QSpinBox(Form)
        self.time1.setGeometry(QtCore.QRect(310, 30, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.time1.setFont(font)
        self.time1.setMaximum(32768)
        self.time1.setProperty("value", 180)
        self.time1.setObjectName("time1")
        self.second1 = QtWidgets.QLabel(Form)
        self.second1.setGeometry(QtCore.QRect(420, 30, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.second1.setFont(font)
        self.second1.setObjectName("second1")
        self.pointer = QtWidgets.QLabel(Form)
        self.pointer.setGeometry(QtCore.QRect(20, 30, 40, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(30)
        self.pointer.setFont(font)
        self.pointer.setObjectName("pointer")
        self.label2 = QtWidgets.QLabel(Form)
        self.label2.setGeometry(QtCore.QRect(60, 70, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.time2 = QtWidgets.QSpinBox(Form)
        self.time2.setGeometry(QtCore.QRect(310, 70, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.time2.setFont(font)
        self.time2.setMaximum(32768)
        self.time2.setProperty("value", 90)
        self.time2.setObjectName("time2")
        self.second2 = QtWidgets.QLabel(Form)
        self.second2.setGeometry(QtCore.QRect(420, 70, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.second2.setFont(font)
        self.second2.setObjectName("second2")
        self.time3 = QtWidgets.QSpinBox(Form)
        self.time3.setGeometry(QtCore.QRect(310, 110, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.time3.setFont(font)
        self.time3.setMaximum(32768)
        self.time3.setProperty("value", 240)
        self.time3.setObjectName("time3")
        self.label3 = QtWidgets.QLabel(Form)
        self.label3.setGeometry(QtCore.QRect(60, 110, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.second3 = QtWidgets.QLabel(Form)
        self.second3.setGeometry(QtCore.QRect(420, 110, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.second3.setFont(font)
        self.second3.setObjectName("second3")
        self.second3a = QtWidgets.QLabel(Form)
        self.second3a.setGeometry(QtCore.QRect(420, 150, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.second3a.setFont(font)
        self.second3a.setObjectName("second3a")
        self.label3a = QtWidgets.QLabel(Form)
        self.label3a.setGeometry(QtCore.QRect(60, 150, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.label3a.setFont(font)
        self.label3a.setObjectName("label3a")
        self.time3a = QtWidgets.QSpinBox(Form)
        self.time3a.setGeometry(QtCore.QRect(310, 150, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.time3a.setFont(font)
        self.time3a.setMaximum(32768)
        self.time3a.setProperty("value", 240)
        self.time3a.setObjectName("time3a")
        self.time4 = QtWidgets.QSpinBox(Form)
        self.time4.setGeometry(QtCore.QRect(310, 190, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(11)
        self.time4.setFont(font)
        self.time4.setMaximum(32768)
        self.time4.setProperty("value", 180)
        self.time4.setObjectName("time4")
        self.second4 = QtWidgets.QLabel(Form)
        self.second4.setGeometry(QtCore.QRect(420, 190, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.second4.setFont(font)
        self.second4.setObjectName("second4")
        self.label4 = QtWidgets.QLabel(Form)
        self.label4.setGeometry(QtCore.QRect(60, 190, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.startstep = QtWidgets.QPushButton(Form)
        self.startstep.setGeometry(QtCore.QRect(130, 240, 100, 30))
        self.startstep.setObjectName("startstep")
        self.passstep = QtWidgets.QPushButton(Form)
        self.passstep.setGeometry(QtCore.QRect(270, 240, 100, 30))
        self.passstep.setObjectName("passstep")
        self.round = QtWidgets.QLabel(Form)
        self.round.setGeometry(QtCore.QRect(480, 70, 20, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.round.setFont(font)
        self.round.setObjectName("round")
        self.round_text = QtWidgets.QLabel(Form)
        self.round_text.setGeometry(QtCore.QRect(500, 70, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(14)
        self.round_text.setFont(font)
        self.round_text.setObjectName("round_text")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "辩论计时器"))
        self.label1.setText(_translate("Form", "第一阶段：立论陈词，双方各"))
        self.second1.setText(_translate("Form", "秒"))
        self.pointer.setText(_translate("Form", "➜"))
        self.label2.setText(_translate("Form", "第二阶段：攻辩阶段，双方各"))
        self.second2.setText(_translate("Form", "秒，第"))
        self.label3.setText(_translate("Form", "第三阶段：自由辩论，双方各"))
        self.second3.setText(_translate("Form", "秒"))
        self.second3a.setText(_translate("Form", "秒"))
        self.label3a.setText(_translate("Form", "第三阶段：加时辩论，双方各"))
        self.second4.setText(_translate("Form", "秒"))
        self.label4.setText(_translate("Form", "第四阶段：总结陈词，双方各"))
        self.startstep.setText(_translate("Form", "开始"))
        self.passstep.setText(_translate("Form", "跳过"))
        self.round.setText(_translate("Form", "1"))
        self.round_text.setText(_translate("Form", "轮，共4轮"))
