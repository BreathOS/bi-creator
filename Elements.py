class Element:
    def __init__(self, isRequired, description):
        self.isRequired = isRequired
        self.description = description


class File(Element):
    def __init__(self, isRequired, description, src, dest, isDeb):
        super().__init__(isRequired, description)
        self.src = src
        self.dest = dest
        self.iaDeb = isDeb


class Folder(Element):
    def __init__(self, isRequired, description, src, dest):
        self.src = src
        self.dest = dest
        self.isRequired = isRequired
        self.description = description


class Package(Element):
    def __init__(self, isRequired, name):
        super().__init__(isRequired, name)
        self.name = name


class Command(Element):
    def __init__(self, isRequired, description, file):
        super().__init__(isRequired, description)
        self.file = file