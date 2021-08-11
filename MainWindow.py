from functools import partial

import PyQt6.QtCore
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox

from BiPackage import BiPackage
from controllers.FileController import FileController
from controllers.FolderController import FolderController
from Elements import Element


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/mainwindow.ui', self)
        self.show()
        self.packageElement = None
        self.biPackage = None
        self.addButton.clicked.connect(self.addElement)
        self.createPackageButton.clicked.connect(self.createPackage)
        self.saveChangesButton.clicked.connect(self.saveChanges)
        self.cancelButton.clicked.connect(self.cancel)

    def addElement(self):
        if self.packageElement is None:
            curOption = self.elementType.currentText()
            if curOption == 'File':
                self.packageElement = FileController()
            if curOption == 'Folder':
                self.packageElement = FolderController()
        self.packageElement.newElement.connect(self.addElementGui)
        self.packageElement.show()

    def createPackage(self):
        self.biPackage = BiPackage()
        self.elementType.setEnabled(True)
        self.addButton.setEnabled(True)
        self.saveChangesButton.setEnabled(True)
        self.cancelButton.setEnabled(True)
        self.createPackageButton.setEnabled(False)
        self.biPackageName.setEnabled(True)
        self.biPackageVersion.setEnabled(True)

    def saveChanges(self):
        name = self.biPackageName.text()
        version = self.biPackageVersion.text()
        if len(self.biPackage.getElements()) == 0:
            QMessageBox().critical(self, "Error", "Suitcase cannot be empty")
        elif not name or name.isspace():
            QMessageBox().critical(self, "Error", "Suitcase should have a name")
        elif not version or version.isspace():
            QMessageBox().critical(self, "Error", "Suitcase should have a version")
        else:
            path = QFileDialog.getSaveFileName(self, 'Save File', '',
                                        '.json')[0]
            self.biPackage.setName(name)
            self.biPackage.setVersion(version)
            with open(path + '.json', 'w') as manifest:
                manifest.write(self.biPackage.toJson())

    def cancel(self):
        self.elementType.setEnabled(False)
        self.addButton.setEnabled(False)
        self.saveChangesButton.setEnabled(False)
        self.cancelButton.setEnabled(False)
        self.createPackageButton.setEnabled(True)
        self.biPackageName.setEnabled(False)
        self.biPackageVersion.setEnabled(False)

    def uploadPackageToGui(self):
        for i in reversed(range(self.elements.count())):
            self.elements.itemAt(i).widget().deleteLater()
        elements = self.biPackage.getElements()
        for i in range(len(elements)):
            self.elements.addWidget(QLabel(elements[i].description), i, 0)
            btn = QPushButton('Remove')
            btn.clicked.connect(partial(self.biPackage.deleteElement, i))
            btn.clicked.connect(self.uploadPackageToGui)
            self.elements.addWidget(btn, i, 1)

    @PyQt6.QtCore.pyqtSlot(Element)
    def addElementGui(self, element):
        self.biPackage.addElement(element)
        self.uploadPackageToGui()
        self.packageElement.newElement.disconnect()

