from functools import partial

from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QFileDialog, QMessageBox, QWidget
from PyQt6.QtCore import QThread, Qt, pyqtSlot

from BiPackage import BiPackage
from PackageCreator import PackageCreator
from controllers.FileController import FileController
from controllers.FolderController import FolderController
from controllers.PackageController import PackageController
from Elements import Element


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.msg = LoadingScreen()
        uic.loadUi('forms/mainwindow.ui', self)
        self.show()
        self.packageElement = None
        self.biPackage = None
        self.creator = None
        self.addButton.clicked.connect(self.addElement)
        self.createPackageButton.clicked.connect(self.createPackage)
        self.saveChangesButton.clicked.connect(self.saveChanges)
        self.cancelButton.clicked.connect(self.cancel)
        self.elementType.activated.connect(self.typeSelected)
        self.worker = QThread()

    def typeSelected(self):
        curOption = self.elementType.currentText()
        if curOption == 'Select type':
            self.addButton.setEnabled(False)
        else:
            self.addButton.setEnabled(True)

    def addElement(self):
        curOption = self.elementType.currentText()
        if curOption == 'File':
            self.packageElement = FileController()
        if curOption == 'Folder':
            self.packageElement = FolderController()
        if curOption == 'Package':
            self.packageElement = PackageController()
        self.packageElement.newElement.connect(self.addElementGui)
        self.packageElement.show()

    def createPackage(self):
        self.biPackage = BiPackage()
        self.elementType.setEnabled(True)
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
            path = QFileDialog.getSaveFileName(self, 'Save File', name, '.bi')[0]
            if path != '':
                self.biPackage.setName(name)
                self.biPackage.setVersion(version)
                self.creator = PackageCreator(self.biPackage, path)
                self.worker.started.connect(self.msg.show)
                self.worker.finished.connect(self.creator.deleteLater)

                self.worker.started.connect(self.creator.start)
                self.creator.finished.connect(self.worker.quit)
                self.worker.finished.connect(self.msg.close)
                self.worker.finished.connect(self.creator.deleteLater)
                self.creator.moveToThread(self.worker)
                self.worker.start()

    def cancel(self):
        self.elementType.setEnabled(False)
        self.addButton.setEnabled(False)
        self.saveChangesButton.setEnabled(False)
        self.cancelButton.setEnabled(False)
        self.createPackageButton.setEnabled(True)
        self.biPackageName.setEnabled(False)
        self.biPackageVersion.setEnabled(False)
        self.elementType.setCurrentIndex(0)

    def uploadPackageToGui(self):
        for i in reversed(range(self.elements.count())):
            self.elements.itemAt(i).widget().deleteLater()
        elements = self.biPackage.getElements()
        for i in range(len(elements)):
            (elementType, element), = elements[i].items()
            self.elements.addWidget(QLabel(element.description), i, 0)
            btn = QPushButton('Remove')
            btn.clicked.connect(partial(self.biPackage.deleteElement, i))
            btn.clicked.connect(self.uploadPackageToGui)
            self.elements.addWidget(btn, i, 1)

    @pyqtSlot(Element)
    def addElementGui(self, element):
        self.biPackage.addElement(element)
        self.uploadPackageToGui()
        self.packageElement.newElement.disconnect()
        self.elementType.setCurrentIndex(0)


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/loadingscreen.ui', self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint |
                          Qt.WindowType.CustomizeWindowHint |
                          Qt.WindowType.FramelessWindowHint)
