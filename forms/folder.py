# Form implementation generated from reading ui file 'folder.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddFolderMenu(object):
    def setupUi(self, AddFolderMenu):
        AddFolderMenu.setObjectName("AddFolderMenu")
        AddFolderMenu.resize(400, 216)
        self.gridLayout = QtWidgets.QGridLayout(AddFolderMenu)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.chooseFolderButton = QtWidgets.QPushButton(AddFolderMenu)
        self.chooseFolderButton.setObjectName("chooseFolderButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.chooseFolderButton)
        self.folderPath = QtWidgets.QLineEdit(AddFolderMenu)
        self.folderPath.setObjectName("folderPath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.folderPath)
        self.label_2 = QtWidgets.QLabel(AddFolderMenu)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.destinationPath = QtWidgets.QLineEdit(AddFolderMenu)
        self.destinationPath.setObjectName("destinationPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.destinationPath)
        self.label_4 = QtWidgets.QLabel(AddFolderMenu)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.description = QtWidgets.QLineEdit(AddFolderMenu)
        self.description.setObjectName("description")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.description)
        self.verticalLayout.addLayout(self.formLayout)
        self.useHome = QtWidgets.QCheckBox(AddFolderMenu)
        self.useHome.setChecked(True)
        self.useHome.setObjectName("useHome")
        self.verticalLayout.addWidget(self.useHome)
        self.isRequired = QtWidgets.QCheckBox(AddFolderMenu)
        self.isRequired.setChecked(True)
        self.isRequired.setObjectName("isRequired")
        self.verticalLayout.addWidget(self.isRequired)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancelButton = QtWidgets.QPushButton(AddFolderMenu)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        self.addFolder = QtWidgets.QPushButton(AddFolderMenu)
        self.addFolder.setObjectName("addFolder")
        self.horizontalLayout.addWidget(self.addFolder)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(AddFolderMenu)
        QtCore.QMetaObject.connectSlotsByName(AddFolderMenu)

    def retranslateUi(self, AddFolderMenu):
        _translate = QtCore.QCoreApplication.translate
        AddFolderMenu.setWindowTitle(_translate("AddFolderMenu", "Add folder"))
        self.chooseFolderButton.setText(_translate("AddFolderMenu", "Choose folder"))
        self.label_2.setText(_translate("AddFolderMenu", "Install to:"))
        self.label_4.setText(_translate("AddFolderMenu", "Description"))
        self.useHome.setText(_translate("AddFolderMenu", "Use home folder as root"))
        self.isRequired.setText(_translate("AddFolderMenu", "Required"))
        self.cancelButton.setText(_translate("AddFolderMenu", "Cancel"))
        self.addFolder.setText(_translate("AddFolderMenu", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddFolderMenu = QtWidgets.QWidget()
    ui = Ui_AddFolderMenu()
    ui.setupUi(AddFolderMenu)
    AddFolderMenu.show()
    sys.exit(app.exec())