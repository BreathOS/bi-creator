# Form implementation generated from reading ui file 'package.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddPackageMenu(object):
    def setupUi(self, AddPackageMenu):
        AddPackageMenu.setObjectName("AddPackageMenu")
        AddPackageMenu.resize(532, 309)
        self.gridLayout_2 = QtWidgets.QGridLayout(AddPackageMenu)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pathToDeb = QtWidgets.QLineEdit(AddPackageMenu)
        self.pathToDeb.setObjectName("pathToDeb")
        self.gridLayout_2.addWidget(self.pathToDeb, 2, 2, 1, 2)
        self.isDeb = QtWidgets.QRadioButton(AddPackageMenu)
        self.isDeb.setObjectName("isDeb")
        self.gridLayout_2.addWidget(self.isDeb, 3, 2, 1, 1)
        self.chooseFile = QtWidgets.QPushButton(AddPackageMenu)
        self.chooseFile.setObjectName("chooseFile")
        self.gridLayout_2.addWidget(self.chooseFile, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(AddPackageMenu)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.aptPackageName = QtWidgets.QLineEdit(AddPackageMenu)
        self.aptPackageName.setObjectName("aptPackageName")
        self.gridLayout_2.addWidget(self.aptPackageName, 0, 2, 1, 2)
        self.isApt = QtWidgets.QRadioButton(AddPackageMenu)
        self.isApt.setObjectName("isApt")
        self.gridLayout_2.addWidget(self.isApt, 1, 2, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(AddPackageMenu)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 1, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(AddPackageMenu)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 1, 0, 1, 1)
        self.isRequired = QtWidgets.QCheckBox(AddPackageMenu)
        self.isRequired.setChecked(True)
        self.isRequired.setObjectName("isRequired")
        self.gridLayout.addWidget(self.isRequired, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 4)

        self.retranslateUi(AddPackageMenu)
        QtCore.QMetaObject.connectSlotsByName(AddPackageMenu)

    def retranslateUi(self, AddPackageMenu):
        _translate = QtCore.QCoreApplication.translate
        AddPackageMenu.setWindowTitle(_translate("AddPackageMenu", "Add package"))
        self.isDeb.setText(_translate("AddPackageMenu", ".deb"))
        self.chooseFile.setText(_translate("AddPackageMenu", "Choose .deb-file"))
        self.label_2.setText(_translate("AddPackageMenu", "Package name"))
        self.isApt.setText(_translate("AddPackageMenu", "From APT"))
        self.saveButton.setText(_translate("AddPackageMenu", "Save"))
        self.cancelButton.setText(_translate("AddPackageMenu", "Cancel"))
        self.isRequired.setText(_translate("AddPackageMenu", "Requierd"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddPackageMenu = QtWidgets.QWidget()
    ui = Ui_AddPackageMenu()
    ui.setupUi(AddPackageMenu)
    AddPackageMenu.show()
    sys.exit(app.exec())