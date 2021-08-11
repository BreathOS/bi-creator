from PyQt6 import uic, QtWidgets

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
        dest = self.destinationPath.text().replace('~/', '/')
        if dest[0] != '/':
            dest = '/' + dest
        args = self.isRequired.isChecked(), self.description.text(), self.filePath.text(), dest, self.useHome.isChecked()
        self.isRequired.setChecked(True)
        self.description.clear()
        self.filePath.clear()
        self.destinationPath.clear()
        self.useHome.setChecked(True)
        if not self.isBlank(args):
            self.newElement.emit(File(*args))
            self.close()



