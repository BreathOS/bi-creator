class Element:
    def __init__(self, required, description):
        self.required = required
        self.description = description


class File(Element):
    def __init__(self, required, description, source, destination, usingHome, fileName):
        super().__init__(required, description)
        self.source = source
        self.destination = destination
        self.usingHome = usingHome
        self.fileName = fileName


class Folder(Element):
    def __init__(self, required, description, source, destination, usingHome, folderName):
        self.source = source
        self.destination = destination
        self.required = required
        self.description = description
        self.usingHome = usingHome
        self.folderName = folderName


class Package(Element):
    def __init__(self, required, name, packageType, source):
        super().__init__(required, name)
        self.name = name
        self.packageType = packageType
        self.source = source
