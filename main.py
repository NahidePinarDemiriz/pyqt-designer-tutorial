import PyQt6.QtWidgets as Qtw
import PyQt6.QtGui as Qtg

class MainWindow(Qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("My GUI Project")

        # Set Vertical layout
        self.setLayout(Qtw.QVBoxLayout())

        # Create a Label
        self.my_label = Qtw.QLabel("What's your name?")
        # Change the font size of label
        self.my_label.setFont(Qtg.QFont('Helvetica', 18))
        self.layout().addWidget(self.my_label)

        # Create an entry box
        self.my_entry = Qtw.QLineEdit()
        self.my_entry.setObjectName("name_field")
        self.my_entry.setText("")
        self.layout().addWidget(self.my_entry)

        # Create a button
        my_button = Qtw.QPushButton("Press Me!")
        my_button.clicked.connect(self.press_it)
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

    def press_it(self):
        # Add name to label
        self.my_label.setText(f'Hello {self.my_entry.text()}!')

        # Clear the entry box
        self.my_entry.setText("")

if __name__ == "__main__":
    app = Qtw.QApplication([])
    mw = MainWindow()
    app.exec()