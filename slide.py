from PyQt6.QtWidgets import QMainWindow, QApplication, QSlider, QLabel
from PyQt6 import uic
from PyQt6.QtGui import QFont
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("slider.ui", self)
        self.setWindowTitle("Slider")

        # Define our widgets
        self.slider = self.findChild(QSlider, "horizontalSlider")
        self.label = self.findChild(QLabel, "label")
        font = QFont()
        font.setPointSize(72)
        self.label.setFont(font)

        # Set Slider Properties
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        self.slider.setValue(0)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(5)
        self.slider.setSingleStep(5)

        # Move the slider
        self.slider.valueChanged.connect(self.slide_it)

        # Show the app
        self.show()

    def slide_it(self, value):
        self.label.setText(str(value))



# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()