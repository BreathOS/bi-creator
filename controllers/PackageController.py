import os

from forms.package import Ui_AddPackageMenu
from PyQt6.QtWidgets import QMessageBox, QFileDialog

from controllers.ElementController import ElementController
from Elements import Package


class PackageController(ElementController):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddPackageMenu()
        self.ui.setupUi(self)
        self.ui.isDeb.toggled.connect(self.setFile)
        self.ui.isApt.toggled.connect(self.setPackage)
        self.ui.chooseFile.clicked.connect(self.openFile)
        self.ui.saveButton.clicked.connect(self.saveElement)
        self.ui.cancelButton.clicked.connect(self.close)

    def setFile(self):
        self.ui.aptPackageName.setEnabled(False)
        self.ui.chooseFile.setEnabled(True)
        self.ui.pathToDeb.setEnabled(True)

    def setPackage(self):
        self.ui.aptPackageName.setEnabled(True)
        self.ui.chooseFile.setEnabled(False)
        self.ui.pathToDeb.setEnabled(False)

    def openFile(self):
        self.ui.pathToDeb.setText(QFileDialog.getOpenFileName()[0])

    def saveElement(self):
        if not self.ui.isApt.isChecked() and not self.ui.isDeb.isChecked():
            QMessageBox().critical(self, "Error!", "No package type selected!")
            return
        if self.ui.isApt.isChecked():
            args = self.ui.isRequired.isChecked(), self.ui.aptPackageName.text(), 'apt', 'apt'
            if not self.isBlank(args):
                self.newElement.emit(Package(*args))
                self.close()
        else:
            name = self.ui.pathToDeb.text()[self.ui.pathToDeb.text().rfind('/') + 1:]
            src = self.ui.pathToDeb.text()
            args = self.ui.isRequired.isChecked(), name, 'deb', src
            if not os.path.isfile(src):
                QMessageBox().critical(self, "Error! File does not exist", "File " + src + " does not exist!")
            elif not self.isBlank(args):
                self.newElement.emit(Package(*args))
                self.close()


