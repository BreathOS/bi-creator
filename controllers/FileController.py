import os

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMessageBox

from Elements import File
from controllers.ElementController import ElementController


class FileController(ElementController):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/file.ui', self)
        self.show()
        self.chooseFileButton.clicked.connect(self.openFile)
        self.cancelButton.clicked.connect(self.close)
        self.addFile.clicked.connect(self.saveElement)

    def openFile(self):
        self.filePath.setText(QtWidgets.QFileDialog.getOpenFileName()[0])

    def saveElement(self):
        src = self.filePath.text()
        dest = self.destinationPath.text().replace('~/', '/')
        if not os.path.isfile(src):
            QMessageBox().critical(self, "Error! File does not exist", "File " + src + " does not exist!")
        elif dest.endswith('/'):
            QMessageBox().critical(self, "Error! File does not exist", "Destination should not be a folder")
        else:
            if len(dest) > 0 and dest[0] != '/':
                dest = '/' + dest
            args = self.isRequired.isChecked(), self.description.text(), src, dest, self.useHome.isChecked()
            self.isRequired.setChecked(True)
            self.description.clear()
            self.filePath.clear()
            self.destinationPath.clear()
            self.useHome.setChecked(True)
            if not self.isBlank(args):
                self.newElement.emit(File(*args))
                self.close()



