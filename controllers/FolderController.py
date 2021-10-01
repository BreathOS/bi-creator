import os

from forms.folder import Ui_AddFolderMenu
from PyQt6.QtWidgets import QFileDialog, QMessageBox

from Elements import Folder
from controllers.ElementController import ElementController


class FolderController(ElementController):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AddFolderMenu()
        self.ui.setupUi(self)
        self.ui.chooseFolderButton.clicked.connect(self.openFolder)
        self.ui.cancelButton.clicked.connect(self.close)
        self.ui.addFolder.clicked.connect(self.saveElement)

    def openFolder(self):
        self.ui.folderPath.setText(QFileDialog.getExistingDirectory())

    def saveElement(self):
        src = self.ui.folderPath.text()
        dest = self.ui.destinationPath.text().replace('~/', '/')
        if src.endswith('/'):
            src = src[:-1]
        folderName = src[src.rfind('/') + 1:]
        if not dest.endswith('/'):
            dest += '/'
        if not os.path.isdir(src):
            QMessageBox().critical(self, "Error! Folder does not exist", "Folder " + src + " does not exist!")
        else:
            if len(dest) > 0 and dest[0] != '/':
                dest = '/' + dest
            args = self.ui.isRequired.isChecked(), self.ui.description.text(), src, dest, self.ui.useHome.isChecked(), folderName
            self.ui.isRequired.setChecked(True)
            self.ui.description.clear()
            self.ui.folderPath.clear()
            self.ui.destinationPath.clear()
            self.ui.useHome.setChecked(True)
            if not self.isBlank(args):
                self.newElement.emit(Folder(*args))
                self.close()
