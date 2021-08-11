import os

from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog, QMessageBox

from Elements import Folder
from controllers.ElementController import ElementController


class FolderController(ElementController):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/folder.ui', self)
        self.show()
        self.chooseFolderButton.clicked.connect(self.openFolder)
        self.cancelButton.clicked.connect(self.close)
        self.addFolder.clicked.connect(self.saveElement)

    def openFolder(self):
        self.folderPath.setText(QFileDialog.getExistingDirectory())

    def saveElement(self):
        src = self.folderPath.text()
        dest = self.destinationPath.text().replace('~/', '/')
        if not os.path.isdir(src):
            QMessageBox().critical(self, "Error! File does not exist", "Folder " + src + " does not exist!")
        else:
            if len(dest) > 0 and dest[0] != '/':
                dest = '/' + dest
            args = self.isRequired.isChecked(), self.description.text(), src, dest, self.useHome.isChecked()
            self.isRequired.setChecked(True)
            self.description.clear()
            self.folderPath.clear()
            self.destinationPath.clear()
            self.useHome.setChecked(True)
            if not self.isBlank(args):
                self.newElement.emit(Folder(*args))
                self.close()
