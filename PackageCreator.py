import os
from shutil import copy2

from PyQt6.QtCore import QObject, pyqtSignal

from BiPackage import BiPackage
from Elements import *


class PackageCreator (QObject):
    finished = pyqtSignal()

    def __init__(self, biPackage: BiPackage, path: str):
        super().__init__()
        self.biPackage = biPackage
        self.path = path

        self.createDirs()
        self.addElements()
        self.writeManifset()

    def createDirs(self):
        os.mkdir(self.path)
        if not self.path.endswith('/'):
            self.path += '/'
        os.mkdir(self.path + 'pkgs')
        os.mkdir(self.path + 'cfgs')

    def addElements(self):
        for i in self.biPackage.getElements():
            if isinstance(i, File):
                destFile = self.path + 'cfgs/' + i.description + i.dest
                destFolder = self.path + 'cfgs/' + i.description + i.dest[:i.dest.rfind('/')]
                os.makedirs(destFolder)
                copy2(i.src, destFile)

    def writeManifset(self):
        with open(self.path + self.biPackage.name + '.json', 'w') as manifest:
            manifest.write(self.biPackage.toJson())
