from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(209, 196)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 107, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.blue_checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(60, 40, 68, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blue_checkBox.setFont(font)
        self.blue_checkBox.setObjectName("blue_checkBox")
        self.red_checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(60, 10, 63, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.red_checkBox.setFont(font)
        self.red_checkBox.setObjectName("red_checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 209, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Update check boxes
        self.red_checkBox.stateChanged.connect(lambda: self.checked())
        self.blue_checkBox.toggled.connect(lambda: self.checked())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pick a color"))
        self.blue_checkBox.setText(_translate("MainWindow", "Blue"))
        self.red_checkBox.setText(_translate("MainWindow", "Red"))

    def checked(self):
        if self.red_checkBox.isChecked() == True:
            self.red = "Red"
        else:
            self.red = ''

        if self.blue_checkBox.isChecked() == True:
            self.blue = "Blue"
        else:
            self.blue = ''

        self.label.setText(f'{self.red} {self.blue}')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
