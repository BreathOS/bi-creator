# Form implementation generated from reading ui file 'loadingscreen.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoadScreenWindow(object):
    def setupUi(self, LoadScreenWindow):
        LoadScreenWindow.setObjectName("LoadScreenWindow")
        LoadScreenWindow.resize(280, 200)
        LoadScreenWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.gridLayout_3 = QtWidgets.QGridLayout(LoadScreenWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(LoadScreenWindow)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(LoadScreenWindow)
        QtCore.QMetaObject.connectSlotsByName(LoadScreenWindow)

    def retranslateUi(self, LoadScreenWindow):
        _translate = QtCore.QCoreApplication.translate
        LoadScreenWindow.setWindowTitle(_translate("LoadScreenWindow", "Form"))
        self.label.setText(_translate("LoadScreenWindow", "Processing..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoadScreenWindow = QtWidgets.QWidget()
    ui = Ui_LoadScreenWindow()
    ui.setupUi(LoadScreenWindow)
    LoadScreenWindow.show()
    sys.exit(app.exec())