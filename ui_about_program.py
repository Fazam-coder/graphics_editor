# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_program.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 409)
        self.text_program = QtWidgets.QTextBrowser(Form)
        self.text_program.setEnabled(True)
        self.text_program.setGeometry(QtCore.QRect(5, 0, 501, 401))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.text_program.setFont(font)
        self.text_program.setPlaceholderText("")
        self.text_program.setObjectName("text_program")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "О программе"))
