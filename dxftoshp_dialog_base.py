# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dxftoshp_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dxftoshpDialogBase(object):
    def setupUi(self, dxftoshpDialogBase):
        dxftoshpDialogBase.setObjectName("dxftoshpDialogBase")
        dxftoshpDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(dxftoshpDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mFieldComboBox = gui.QgsFieldComboBox(dxftoshpDialogBase)
        self.mFieldComboBox.setGeometry(QtCore.QRect(110, 80, 160, 27))
        self.mFieldComboBox.setObjectName("mFieldComboBox")
        self.mFieldComboBox_2 = gui.QgsFieldComboBox(dxftoshpDialogBase)
        self.mFieldComboBox_2.setGeometry(QtCore.QRect(110, 120, 160, 27))
        self.mFieldComboBox_2.setObjectName("mFieldComboBox_2")
        self.mQgsFileWidget = gui.QgsFileWidget(dxftoshpDialogBase)
        self.mQgsFileWidget.setGeometry(QtCore.QRect(110, 30, 201, 27))
        self.mQgsFileWidget.setObjectName("mQgsFileWidget")
        self.mQgsFileWidget_2 = gui.QgsFileWidget(dxftoshpDialogBase)
        self.mQgsFileWidget_2.setGeometry(QtCore.QRect(110, 180, 201, 27))
        self.mQgsFileWidget_2.setObjectName("mQgsFileWidget_2")
        self.label = QtWidgets.QLabel(dxftoshpDialogBase)
        self.label.setGeometry(QtCore.QRect(110, 10, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dxftoshpDialogBase)
        self.label_2.setGeometry(QtCore.QRect(110, 60, 131, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dxftoshpDialogBase)
        self.label_3.setGeometry(QtCore.QRect(110, 160, 121, 18))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(dxftoshpDialogBase)
        self.button_box.accepted.connect(dxftoshpDialogBase.accept)
        self.button_box.rejected.connect(dxftoshpDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(dxftoshpDialogBase)

    def retranslateUi(self, dxftoshpDialogBase):
        _translate = QtCore.QCoreApplication.translate
        dxftoshpDialogBase.setWindowTitle(_translate("dxftoshpDialogBase", "dxftoshp"))
        self.label.setText(_translate("dxftoshpDialogBase", "Input dxf filename"))
        self.label_2.setText(_translate("dxftoshpDialogBase", "Select contour layer"))
        self.label_3.setText(_translate("dxftoshpDialogBase", "Output Shape file"))


from qgis import gui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dxftoshpDialogBase = QtWidgets.QDialog()
    ui = Ui_dxftoshpDialogBase()
    ui.setupUi(dxftoshpDialogBase)
    dxftoshpDialogBase.show()
    sys.exit(app.exec_())
