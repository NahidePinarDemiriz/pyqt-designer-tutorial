from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(230, 203)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.red_checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(70, 10, 63, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.red_checkBox.setFont(font)
        self.red_checkBox.setObjectName("red_checkBox")
        self.blue_checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(70, 40, 68, 29))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blue_checkBox.setFont(font)
        self.blue_checkBox.setObjectName("blue_checkBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 110, 107, 25))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.clicked.connect(lambda: self.checked())
        self.pushButton.setGeometry(QtCore.QRect(50, 70, 116, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 230, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Set red checked by default
        # self.red_checkBox.setChecked(True)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red_checkBox.setText(_translate("MainWindow", "Red"))
        self.blue_checkBox.setText(_translate("MainWindow", "Blue"))
        self.label.setText(_translate("MainWindow", "Pick a color"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))

    def checked(self):
        # States: 0=not clicked; 2=checked
        print(self.red_checkBox.checkState())

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
