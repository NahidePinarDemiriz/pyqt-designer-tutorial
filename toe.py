from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt6 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("toe.ui", self)

        # Define a counter to keep track of who's turn it is!
        self.counter = 0

        # Define our widgets
        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")

        self.label = self.findChild(QLabel, "label")

        # Click the button
        self.button1.clicked.connect(lambda: self.clicker(self.button1))
        self.button2.clicked.connect(lambda: self.clicker(self.button2))
        self.button3.clicked.connect(lambda: self.clicker(self.button3))
        self.button4.clicked.connect(lambda: self.clicker(self.button4))
        self.button5.clicked.connect(lambda: self.clicker(self.button5))
        self.button6.clicked.connect(lambda: self.clicker(self.button6))
        self.button7.clicked.connect(lambda: self.clicker(self.button7))
        self.button8.clicked.connect(lambda: self.clicker(self.button8))
        self.button9.clicked.connect(lambda: self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)

        # Show the app
        self.show()

    def checkWin(self):
        # Across
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1, self.button4, self.button7)

        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2, self.button5, self.button8)

        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3, self.button6, self.button9)

        # Down
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1, self.button2, self.button3)

        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4, self.button5, self.button6)

        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7, self.button8, self.button9)

        # Diagonal
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1, self.button5, self.button9)

        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3, self.button5, self.button7)

    def win(self, a,b,c):
        # Change the button colors to red
        a.setStyleSheet('QPushButton {color: red;}')
        b.setStyleSheet('QPushButton {color: red;}')
        c.setStyleSheet('QPushButton {color: red;}')

        # Add winner label
        self.label.setText(f"{a.text()} Wins!")

        # Disable the board
        self.disable()

    # Disable the board
    def disable(self):
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9, ]

        # Reset the buttons
        for b in button_list:
            b.setEnabled(False)

    # Click the buttons
    def clicker(self, b):
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False)

        # Increment the counter
        self.counter += 1

        # Check if won
        self.checkWin()

    # Start Over
    def reset(self):
        # Create a list of all our buttons
        button_list = [
        self.button1,
        self.button2,
        self.button3,
        self.button4,
        self.button5,
        self.button6,
        self.button7,
        self.button8,
        self.button9,]

        # Reset the buttons
        for b in button_list:
            b.setText("")
            b.setEnabled(True)
            # Reset the button colors
            b.setStyleSheet('QPushButton {color: #797979;}')


        # Reset the label
        self.label.setText("X Goes First!")

        # Reset the counter
        self.counter = 0


# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec()