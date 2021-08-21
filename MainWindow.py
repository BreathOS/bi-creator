from functools import partial

from forms.mainwindow import Ui_MainMenu
from forms.loadingscreen import Ui_LoadScreenWindow

from PyQt6 import QtCore
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
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        self.packageElement = None
        self.biPackage = None
        self.creator = None
        self.ui.addButton.clicked.connect(self.addElement)
        self.ui.createPackageButton.clicked.connect(self.createPackage)
        self.ui.saveChangesButton.clicked.connect(self.saveChanges)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.elementType.activated.connect(self.typeSelected)
        self.worker = QThread()

    def typeSelected(self):
        curOption = self.ui.elementType.currentText()
        if curOption == 'Select type':
            self.ui.addButton.setEnabled(False)
        else:
            self.ui.addButton.setEnabled(True)

    def addElement(self):
        curOption = self.ui.elementType.currentText()
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
        self.ui.elementType.setEnabled(True)
        self.ui.saveChangesButton.setEnabled(True)
        self.ui.cancelButton.setEnabled(True)
        self.ui.createPackageButton.setEnabled(False)
        self.ui.biPackageName.setEnabled(True)
        self.ui.biPackageVersion.setEnabled(True)

    def saveChanges(self):
        name = self.ui.biPackageName.text()
        version = self.ui.biPackageVersion.text()
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
        self.ui.elementType.setEnabled(False)
        self.ui.addButton.setEnabled(False)
        self.ui.saveChangesButton.setEnabled(False)
        self.ui.cancelButton.setEnabled(False)
        self.ui.createPackageButton.setEnabled(True)
        self.ui.biPackageName.setEnabled(False)
        self.ui.biPackageVersion.setEnabled(False)
        self.ui.elementType.setCurrentIndex(0)

    def uploadPackageToGui(self):
        for i in reversed(range(self.ui.elements.count())):
            self.ui.elements.itemAt(i).widget().deleteLater()
        elements = self.biPackage.getElements()
        for i in range(len(elements)):
            (elementType, element), = elements[i].items()
            self.ui.elements.addWidget(QLabel(element.description), i, 0)
            btn = QPushButton('Remove')
            btn.clicked.connect(partial(self.biPackage.deleteElement, i))
            btn.clicked.connect(self.uploadPackageToGui)
            self.ui.elements.addWidget(btn, i, 1)

    @pyqtSlot(Element)
    def addElementGui(self, element):
        self.biPackage.addElement(element)
        self.uploadPackageToGui()
        self.packageElement.newElement.disconnect()
        self.ui.elementType.setCurrentIndex(0)


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoadScreenWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint |
                          Qt.WindowType.CustomizeWindowHint |
                          Qt.WindowType.FramelessWindowHint)
