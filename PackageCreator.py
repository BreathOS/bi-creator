import os
from shutil import copy2, copytree, make_archive, rmtree

from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

from BiPackage import BiPackage
from Elements import *


class PackageCreator (QObject):
    finished = pyqtSignal()

    def __init__(self, biPackage: BiPackage, path: str):
        super().__init__()
        self.biPackage = biPackage
        self.path = path

    @pyqtSlot()
    def start(self):
        self.createDirs()
        self.addElements()
        self.writeManifset()
        self.createBi()
        self.finished.emit()

    def createBi(self):
        path = self.path
        if path.endswith('/'):
            path = path[:-1]
        make_archive(path, 'zip', self.path)
        rmtree(path)
        os.rename(path + '.zip', path + '.bi')

    def createDirs(self):
        os.mkdir(self.path)
        if not self.path.endswith('/'):
            self.path += '/'
        os.mkdir(self.path + 'packages')
        os.mkdir(self.path + 'configurations')

    def addElements(self):
        for i in self.biPackage.getElements():
            (elementType, element), = i.items()
            if isinstance(element, File):
                destFolder = self.path + 'configurations/' + element.description
                os.makedirs(destFolder)
                copy2(element.source, destFolder)
            if isinstance(element, Folder):
                dest = self.path + 'configurations/' + element.description + element.source[element.source.rfind('/'):]
                copytree(element.source, dest)
            if isinstance(element, Package):
                if element.packageType == 'deb':
                    dest = self.path + 'packages/' + element.description
                    copy2(element.source, dest)

    def writeManifset(self):
        with open(self.path + self.biPackage.name + '.json', 'w') as manifest:
            manifest.write(self.biPackage.toJson())
