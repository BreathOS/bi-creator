import os

from forms.file import Ui_AddFileMenu
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

from Elements import File
from controllers.ElementController import ElementController


class FileController(ElementController):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddFileMenu()
        self.ui.setupUi(self)
        self.ui.chooseFileButton.clicked.connect(self.openFile)
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.addFile.clicked.connect(self.saveElement)

    def openFile(self):
        self.ui.filePath.setText(QtWidgets.QFileDialog.getOpenFileName()[0])

    def saveElement(self):
        src = self.ui.filePath.text()
        dest = self.ui.destinationPath.text().replace('~/', '/')
        if not os.path.isfile(src):
            QMessageBox().critical(self, "Error! File does not exist", "File " + src + " does not exist!")
        elif dest.endswith('/'):
            QMessageBox().critical(self, "Error! File does not exist", "Destination should not be a folder")
        else:
            if len(dest) > 0 and dest[0] != '/':
                dest = '/' + dest
            args = self.ui.isRequired.isChecked(), self.ui.description.text(), src, dest, self.ui.useHome.isChecked()
            self.ui.isRequired.setChecked(True)
            self.ui.description.clear()
            self.ui.filePath.clear()
            self.ui.destinationPath.clear()
            self.ui.useHome.setChecked(True)
            if not self.isBlank(args):
                self.newElement.emit(File(*args))
                self.close()



