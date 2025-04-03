from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLCDNumber
from PyQt6 import uic
import sys
from PyQt6.QtCore import QTime, QTimer
from datetime import datetime

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("lcd.ui", self)

        # Define our widgets
        self.lcd = self.findChild(QLCDNumber, "lcdNumber")

        # Create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)

        # Start the timer and update every second
        self.timer.start(1000)

        # Call the LCD function
        self.lcd_number()

        # Show the app
        self.show()

    def lcd_number(self):
        # Get the time
        time = datetime.now()
        formatted_time = time.strftime("%I:%M:%S %p")

        # Set number of LCD digits
        self.lcd.setDigitCount(12)
        # Make text flat (no white outline)
        self.lcd.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        # Display the time
        self.lcd.display(formatted_time)

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()