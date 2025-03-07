from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 297)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_me_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.click_me_button.setGeometry(QtCore.QRect(30, 130, 301, 91))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.click_me_button.setFont(font)
        self.click_me_button.setStyleSheet("QPushButton#click_me_button {\n"
"    background-color: red;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.click_me_button.setObjectName("click_me_button")
        self.click_me_button.clicked.connect(self.press_it)
        self.hello_world_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.hello_world_label.setGeometry(QtCore.QRect(90, 30, 171, 81))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(24)
        self.hello_world_label.setFont(font)
        self.hello_world_label.setStyleSheet("")
        self.hello_world_label.setObjectName("hello_world_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # Press the button
    def press_it(self):
        self.hello_world_label.setText("You are \nprecious")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.click_me_button.setText(_translate("MainWindow", "I have a message for you 🤍 Click Me!"))
        self.hello_world_label.setText(_translate("MainWindow", "Hello World! "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
