# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1238, 854)
        Form.setAutoFillBackground(False)
        self.label_r = QtWidgets.QLabel(Form)
        self.label_r.setGeometry(QtCore.QRect(640, 140, 400, 200))
        self.label_r.setScaledContents(False)
        self.label_r.setOpenExternalLinks(False)
        self.label_r.setObjectName("label_r")
        self.label_l = QtWidgets.QLabel(Form)
        self.label_l.setGeometry(QtCore.QRect(100, 130, 400, 200))
        self.label_l.setObjectName("label_l")
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setGeometry(QtCore.QRect(1010, 10, 161, 28))
        self.b1.setObjectName("b1")
        self.path_back = QtWidgets.QTextBrowser(Form)
        self.path_back.setGeometry(QtCore.QRect(100, 10, 801, 31))
        self.path_back.setObjectName("path_back")
        self.path_top = QtWidgets.QTextBrowser(Form)
        self.path_top.setGeometry(QtCore.QRect(100, 50, 801, 31))
        self.path_top.setObjectName("path_top")
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setGeometry(QtCore.QRect(1010, 50, 161, 28))
        self.b2.setObjectName("b2")
        self.lb_up = QtWidgets.QPushButton(Form)
        self.lb_up.setGeometry(QtCore.QRect(210, 390, 93, 28))
        self.lb_up.setObjectName("lb_up")
        self.lb_down = QtWidgets.QPushButton(Form)
        self.lb_down.setGeometry(QtCore.QRect(210, 430, 93, 28))
        self.lb_down.setObjectName("lb_down")
        self.rb_up = QtWidgets.QPushButton(Form)
        self.rb_up.setGeometry(QtCore.QRect(780, 380, 93, 28))
        self.rb_up.setObjectName("rb_up")
        self.rb_down = QtWidgets.QPushButton(Form)
        self.rb_down.setGeometry(QtCore.QRect(780, 420, 93, 28))
        self.rb_down.setObjectName("rb_down")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(300, 470, 520, 220))
        self.label_3.setObjectName("label_3")
        self.llb_up = QtWidgets.QPushButton(Form)
        self.llb_up.setGeometry(QtCore.QRect(210, 730, 93, 28))
        self.llb_up.setObjectName("llb_up")
        self.rrb_down = QtWidgets.QPushButton(Form)
        self.rrb_down.setGeometry(QtCore.QRect(790, 730, 93, 28))
        self.rrb_down.setObjectName("rrb_down")
        self.hand_to = QtWidgets.QPushButton(Form)
        self.hand_to.setGeometry(QtCore.QRect(210, 770, 93, 28))
        self.hand_to.setObjectName("hand_to")
        self.auto_to = QtWidgets.QPushButton(Form)
        self.auto_to.setGeometry(QtCore.QRect(790, 770, 93, 28))
        self.auto_to.setObjectName("auto_to")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_r.setText(_translate("Form", "前景图片显示"))
        self.label_l.setText(_translate("Form", "背景图片显示"))
        self.b1.setText(_translate("Form", "选择背景文件夹"))
        self.b2.setText(_translate("Form", "选择前景文件夹"))
        self.lb_up.setText(_translate("Form", "上一张"))
        self.lb_down.setText(_translate("Form", "下一张"))
        self.rb_up.setText(_translate("Form", "上一张"))
        self.rb_down.setText(_translate("Form", "下一张"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.llb_up.setText(_translate("Form", "上一张"))
        self.rrb_down.setText(_translate("Form", "下一张"))
        self.hand_to.setText(_translate("Form", "手动生成"))
        self.auto_to.setText(_translate("Form", "演化生成"))
