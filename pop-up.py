from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 333)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 411, 291))
        self.stackedWidget.setObjectName("stackedWidget")

        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(parent=self.page)
        self.pushButton.setGeometry(QtCore.QRect(140, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")

        # Ayar paneli
        self.settingsPanel = QtWidgets.QWidget(self.page)
        self.settingsPanel.setGeometry(QtCore.QRect(100, 140, 220, 120))
        self.settingsPanel.setObjectName("settingsPanel")
        self.settingsPanel.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.settingsPanel.setVisible(False)

        # Label
        self.inductanceLabel = QtWidgets.QLabel("Inductance:", self.settingsPanel)
        self.inductanceLabel.setGeometry(QtCore.QRect(10, 10, 100, 20))

        # Değer Gösterimi
        self.inductanceValue = QtWidgets.QLabel("0", self.settingsPanel)
        self.inductanceValue.setGeometry(QtCore.QRect(100, 10, 50, 20))

        # + ve - Butonları
        self.plusButton = QtWidgets.QPushButton("+", self.settingsPanel)
        self.plusButton.setGeometry(QtCore.QRect(160, 10, 20, 20))
        self.minusButton = QtWidgets.QPushButton("-", self.settingsPanel)
        self.minusButton.setGeometry(QtCore.QRect(180, 10, 20, 20))

        # Bobin (animasyon/görsel)
        self.coilBar = QtWidgets.QProgressBar(self.settingsPanel)
        self.coilBar.setGeometry(QtCore.QRect(10, 50, 190, 20))
        self.coilBar.setMinimum(0)
        self.coilBar.setMaximum(100)
        self.coilBar.setValue(0)
        self.coilBar.setFormat("Bobin doluluk: %p%")

        self.stackedWidget.addWidget(self.page)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Endüktans Ayarı"))
        self.pushButton.setText(_translate("MainWindow", "Endüktans"))


class ControlMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.inductance = 0

        self.ui.pushButton.clicked.connect(self.toggleSettingsPanel)
        self.ui.plusButton.clicked.connect(self.increaseInductance)
        self.ui.minusButton.clicked.connect(self.decreaseInductance)

    def toggleSettingsPanel(self):
        isVisible = self.ui.settingsPanel.isVisible()
        self.ui.settingsPanel.setVisible(not isVisible)

    def updateInductanceUI(self):
        self.ui.inductanceValue.setText(str(self.inductance))
        self.ui.coilBar.setValue(self.inductance)

    def increaseInductance(self):
        if self.inductance < 100:
            self.inductance += 10
            self.updateInductanceUI()

    def decreaseInductance(self):
        if self.inductance > 0:
            self.inductance -= 10
            self.updateInductanceUI()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ControlMainWindow()
    MainWindow.show()
    sys.exit(app.exec())
