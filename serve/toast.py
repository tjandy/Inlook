# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toast.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Toast(object):
    def setupUi(self, Toast):
        Toast.setObjectName("Toast")
        Toast.resize(314, 37)
        self.gridLayout = QtWidgets.QGridLayout(Toast)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Toast)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Toast)
        QtCore.QMetaObject.connectSlotsByName(Toast)

    def retranslateUi(self, Toast):
        _translate = QtCore.QCoreApplication.translate
        Toast.setWindowTitle(_translate("Toast", "Form"))
