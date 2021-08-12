class Element:
    def __init__(self, isRequired, description):
        self.isRequired = isRequired
        self.description = description


class File(Element):
    def __init__(self, isRequired, description, src, dest, useHome):
        super().__init__(isRequired, description)
        self.src = src
        self.dest = dest
        self.useHome = useHome


class Folder(Element):
    def __init__(self, isRequired, description, src, dest, useHome):
        self.src = src
        self.dest = dest
        self.isRequired = isRequired
        self.description = description
        self.useHome = useHome


class Package(Element):
    def __init__(self, isRequired, name, packageType, src):
        super().__init__(isRequired, name)
        self.name = name
        self.packageType = packageType
        self.src = src


class Command(Element):
    def __init__(self, isRequired, description, file):
        super().__init__(isRequired, description)
        self.file = file