from PyQt6 import uic
from PyQt6.QtWidgets import QFileDialog

from controllers.ElementController import ElementController


class FolderController(ElementController):
    def __init__(self):
        super().__init__()
        uic.loadUi('forms/folder.ui', self)
        self.show()
        self.chooseFolderButton.clicked.connect(self.openFolder)
        self.cancelButton.clicked.connect(self.cancel)
        self.addFolder.clicked.connect(self.saveElement)

    def openFolder(self):
        folder = QFileDialog.getExistingDirectory()
        self.folderPath.setText(folder)

    def cancel(self):
        self.close()

    def saveElement(self):
        pass