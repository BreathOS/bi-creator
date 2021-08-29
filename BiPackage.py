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
            self.elements.append({type(element).__name__: element})
        else:
            raise TypeError()

    def getElements(self):
        return self.elements

    def deleteAllElements(selfs):
        selfs.elements.clear()

    def deleteElement(self, indx):
        del self.elements[indx]

    def removeRedundantKeys(self, o):
        keys = o.__dict__
        keys.pop('source', None)
        return keys

    def toJson(self):
        return json.dumps(self, default=self.removeRedundantKeys, indent=4, separators=(", ", ": "), sort_keys=True)
