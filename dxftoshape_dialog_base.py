# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dxftoshape_dialog_base.ui'
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
        self.button_box.setGeometry(QtCore.QRect(190, 220, 171, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mQgsFileWidget = gui.QgsFileWidget(dxftoshpDialogBase)
        self.mQgsFileWidget.setGeometry(QtCore.QRect(50, 80, 211, 27))
        self.mQgsFileWidget.setObjectName("mQgsFileWidget")
        self.mComboBox = gui.QgsCheckableComboBox(dxftoshpDialogBase)
        self.mComboBox.setGeometry(QtCore.QRect(50, 160, 211, 27))
        self.mComboBox.setObjectName("mComboBox")
        self.label = QtWidgets.QLabel(dxftoshpDialogBase)
        self.label.setGeometry(QtCore.QRect(50, 60, 191, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dxftoshpDialogBase)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 331, 51))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(dxftoshpDialogBase)
        self.button_box.accepted.connect(dxftoshpDialogBase.accept)
        self.button_box.rejected.connect(dxftoshpDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(dxftoshpDialogBase)

    def retranslateUi(self, dxftoshpDialogBase):
        _translate = QtCore.QCoreApplication.translate
        dxftoshpDialogBase.setWindowTitle(_translate("dxftoshpDialogBase", "dxftoshp"))
        self.label.setText(_translate("dxftoshpDialogBase", "Select a dxf file you want to load"))
        self.label_2.setText(_translate("dxftoshpDialogBase", "Choose contour Layers with elevation or z values "))


from qgis import gui


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dxftoshpDialogBase = QtWidgets.QDialog()
    ui = Ui_dxftoshpDialogBase()
    ui.setupUi(dxftoshpDialogBase)
    dxftoshpDialogBase.show()
    sys.exit(app.exec_())
