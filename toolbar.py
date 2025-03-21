# Form implementation generated from reading ui file 'toolbar.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(394, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 394, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(parent=self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuNew = QtWidgets.QMenu(parent=self.menubar)
        self.menuNew.setObjectName("menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionCut = QtGui.QAction(parent=MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtGui.QAction(parent=MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtGui.QAction(parent=MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionFind = QtGui.QAction(parent=MainWindow)
        self.actionFind.setObjectName("actionFind")
        self.actionFind_Next = QtGui.QAction(parent=MainWindow)
        self.actionFind_Next.setObjectName("actionFind_Next")
        self.actionReplace = QtGui.QAction(parent=MainWindow)
        self.actionReplace.setObjectName("actionReplace")
        self.actionHome = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Downloads/uicons-brands-2.6.0/uicons-brands/svg/fi-brands-youtube.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionHome.setIcon(icon)
        self.actionHome.setObjectName("actionHome")
        self.actionStarbucks = QtGui.QAction(parent=MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Downloads/uicons-brands-2.6.0/uicons-brands/svg/fi-brands-starbucks.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionStarbucks.setIcon(icon1)
        self.actionStarbucks.setObjectName("actionStarbucks")
        self.actionPhotoshop = QtGui.QAction(parent=MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Downloads/uicons-brands-2.6.0/uicons-brands/svg/fi-brands-photoshop.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionPhotoshop.setIcon(icon2)
        self.actionPhotoshop.setObjectName("actionPhotoshop")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionFind)
        self.menuEdit.addAction(self.actionFind_Next)
        self.menuEdit.addAction(self.actionHome)
        self.menuEdit.addAction(self.actionReplace)
        self.menuNew.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuNew.menuAction())
        self.toolBar.addAction(self.actionHome)
        self.toolBar.addAction(self.actionStarbucks)
        self.toolBar.addAction(self.actionPhotoshop)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuNew.setTitle(_translate("MainWindow", "Help"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save As"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionFind_Next.setText(_translate("MainWindow", "Find Next"))
        self.actionReplace.setText(_translate("MainWindow", "Replace"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionStarbucks.setText(_translate("MainWindow", "Starbucks"))
        self.actionPhotoshop.setText(_translate("MainWindow", "Photoshop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
