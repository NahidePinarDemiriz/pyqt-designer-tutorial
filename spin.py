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
        self.my_label = Qtw.QLabel("Pick something from the list below")
        # Change the font size of label
        self.my_label.setFont(Qtg.QFont('Helvetica', 24))
        self.layout().addWidget(self.my_label)

        # Create a Spin box
        self.my_spin = Qtw.QSpinBox(self)
        self.my_spin.setValue(10)  # Set initial value
        self.my_spin.setMaximum(100)  # Set maximum value
        self.my_spin.setMinimum(0)  # Set minimum value
        self.my_spin.setSingleStep(20)  # Set increment/decrement step
        self.my_spin.setPrefix("Your Order is # ")  # Add a prefix
        self.my_spin.setSuffix(" !!!") # Add a suffix
        # Change font size of spin box
        self.my_spin.setFont(Qtg.QFont('Helvetica', 18))

        # Put combo box on the screen
        self.layout().addWidget(self.my_spin)

        # Create a button
        my_button = Qtw.QPushButton("Press Me!")
        my_button.clicked.connect(self.press_it)
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

    def press_it(self):
        # Add name to label
        self.my_label.setText(f'You picked {self.my_spin.value()}!')


if __name__ == "__main__":
    app = Qtw.QApplication([])
    mw = MainWindow()
    app.exec()