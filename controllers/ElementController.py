from abc import abstractmethod
from Elements import Element
from PyQt6 import QtWidgets,  QtCore


class ElementController(QtWidgets.QWidget):
    newElement = QtCore.pyqtSignal(Element)

    def __init__(self):
        super().__init__()

    def isBlank(self, args):
        if args is None or len(args) == 0:
            return True
        for i in args:
            if isinstance(i, str) and (not i or i.isspace()):
                QtWidgets.QMessageBox().critical(self, "Error", "Fields should not be blank")
                return True
        return False

    @abstractmethod
    def saveElement(self):
        pass

