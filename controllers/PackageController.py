import os

from PyQt6 import uic
from PyQt6.QtWidgets import QMessageBox, QFileDialog

from controllers.ElementController import ElementController
from Elements import Package


class PackageController(ElementController):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/package.ui', self)
        self.show()
        self.isDeb.toggled.connect(self.setFile)
        self.isApt.toggled.connect(self.setPackage)
        self.chooseFile.clicked.connect(self.openFile)
        self.saveButton.clicked.connect(self.saveElement)
        self.cancelButton.clicked.connect(self.close)

    def setFile(self):
        self.aptPackageName.setEnabled(False)
        self.chooseFile.setEnabled(True)
        self.pathToDeb.setEnabled(True)

    def setPackage(self):
        self.aptPackageName.setEnabled(True)
        self.chooseFile.setEnabled(False)
        self.pathToDeb.setEnabled(False)

    def openFile(self):
        self.pathToDeb.setText(QFileDialog.getOpenFileName()[0])

    def saveElement(self):
        if not self.isApt.isChecked() and not self.isDeb.isChecked():
            QMessageBox().critical(self, "Error!", "No package type selected!")
            return
        if self.isApt.isChecked():
            args = self.isRequired.isChecked(), self.aptPackageName.text(), 'apt', 'apt'
            if not self.isBlank(args):
                self.newElement.emit(Package(*args))
                self.close()
        else:
            name = self.pathToDeb.text()[self.pathToDeb.text().rfind('/') + 1:]
            src = self.pathToDeb.text()
            args = self.isRequired.isChecked(), name, 'deb', src
            if not os.path.isfile(src):
                QMessageBox().critical(self, "Error! File does not exist", "File " + src + " does not exist!")
            elif not self.isBlank(args):
                self.newElement.emit(Package(*args))
                self.close()


