# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName("MainMenu")
        MainMenu.resize(699, 406)
        self.centralwidget = QtWidgets.QWidget(MainMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.elementType = QtWidgets.QComboBox(self.centralwidget)
        self.elementType.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.elementType.setFont(font)
        self.elementType.setObjectName("elementType")
        self.elementType.addItem("")
        self.elementType.addItem("")
        self.elementType.addItem("")
        self.elementType.addItem("")
        self.horizontalLayout.addWidget(self.elementType)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addButton.sizePolicy().hasHeightForWidth())
        self.addButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.createPackageButton = QtWidgets.QPushButton(self.centralwidget)
        self.createPackageButton.setObjectName("createPackageButton")
        self.horizontalLayout_2.addWidget(self.createPackageButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveChangesButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveChangesButton.setEnabled(False)
        self.saveChangesButton.setObjectName("saveChangesButton")
        self.horizontalLayout_3.addWidget(self.saveChangesButton)
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setEnabled(False)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.widget = QtWidgets.QWidget()
        self.widget.setGeometry(QtCore.QRect(0, 0, 677, 228))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setObjectName("formLayout")
        self.elements = QtWidgets.QGridLayout()
        self.elements.setObjectName("elements")
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.elements)
        self.scrollArea.setWidget(self.widget)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.biPackageName = QtWidgets.QLineEdit(self.centralwidget)
        self.biPackageName.setEnabled(False)
        self.biPackageName.setObjectName("biPackageName")
        self.horizontalLayout_5.addWidget(self.biPackageName)
        self.biPackageVersion = QtWidgets.QLineEdit(self.centralwidget)
        self.biPackageVersion.setEnabled(False)
        self.biPackageVersion.setObjectName("biPackageVersion")
        self.horizontalLayout_5.addWidget(self.biPackageVersion)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainMenu)
        self.statusbar.setObjectName("statusbar")
        MainMenu.setStatusBar(self.statusbar)

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        _translate = QtCore.QCoreApplication.translate
        MainMenu.setWindowTitle(_translate("MainMenu", "Bi-creator"))
        self.elementType.setItemText(0, _translate("MainMenu", "Select type"))
        self.elementType.setItemText(1, _translate("MainMenu", "File"))
        self.elementType.setItemText(2, _translate("MainMenu", "Folder"))
        self.elementType.setItemText(3, _translate("MainMenu", "Package"))
        self.addButton.setText(_translate("MainMenu", "Add"))
        self.createPackageButton.setText(_translate("MainMenu", "Create suitcase"))
        self.saveChangesButton.setText(_translate("MainMenu", "Save"))
        self.cancelButton.setText(_translate("MainMenu", "Cancel"))
        self.biPackageName.setPlaceholderText(_translate("MainMenu", "Suitcase name"))
        self.biPackageVersion.setPlaceholderText(_translate("MainMenu", "Version"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = QtWidgets.QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(MainMenu)
    MainMenu.show()
    sys.exit(app.exec())
