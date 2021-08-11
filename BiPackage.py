from Elements import Element
import json


class BiPackage:
    def __init__(self):
        self.elements = []

    def setName(self, name):
        self.name = name

    def setVersion(self, version):
        self.version = version

    def addElement(self, element: Element):
        if isinstance(element, Element):
            self.elements.append(element)
        else:
            raise TypeError()

    def getElements(self):
        return self.elements

    def deleteElement(self, indx):
        del self.elements[indx]

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, separators=(", ", ": "), sort_keys=True)
