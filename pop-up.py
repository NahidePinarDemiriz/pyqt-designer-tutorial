from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 333)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Stacked Widget
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 411, 291))
        self.stackedWidget.setObjectName("stackedWidget")

        # Page 1
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(parent=self.page)
        self.pushButton.setGeometry(QtCore.QRect(140, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")

        # Ayar paneli (Endüktans ayarları)
        self.settingsPanel = QtWidgets.QWidget(self.page)
        self.settingsPanel.setGeometry(QtCore.QRect(140, 140, 200, 100))
        self.settingsPanel.setObjectName("settingsPanel")
        self.settingsPanel.setStyleSheet("background-color: lightgray; border: 1px solid black;")  # Görünümü
        self.settingsPanel.setVisible(False)  # Başlangıçta görünmesin

        # Endüktans ayarları için bir örnek input
        self.inductanceLabel = QtWidgets.QLabel("Inductance:", self.settingsPanel)
        self.inductanceLabel.setGeometry(QtCore.QRect(10, 10, 100, 20))

        self.inductanceInput = QtWidgets.QLineEdit(self.settingsPanel)
        self.inductanceInput.setGeometry(QtCore.QRect(100, 10, 90, 20))

        self.stackedWidget.addWidget(self.page)

        # Menü ve status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Endüktans"))


class ControlMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ControlMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Butona tıklama fonksiyonu
        self.ui.pushButton.clicked.connect(self.toggleSettingsPanel)

    def toggleSettingsPanel(self):
        # Ayar panelini görünür hale getirme/gizleme
        isVisible = self.ui.settingsPanel.isVisible()
        self.ui.settingsPanel.setVisible(not isVisible)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ControlMainWindow()
    MainWindow.show()
    sys.exit(app.exec())
