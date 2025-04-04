from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt6 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("hover.ui", self)

        # Show the app
        self.show()

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()