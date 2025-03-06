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

        # Create a Combo box
        self.my_combo = Qtw.QComboBox(self)
        self.my_combo.setEditable(True)
        self.my_combo.setInsertPolicy(Qtw.QComboBox.InsertPolicy.InsertAtTop)
        # Add items to the Combo box
        self.my_combo.addItem("Pepperoni", "Something")
        self.my_combo.addItem("Cheese", 2)
        self.my_combo.addItem("Mushroom", Qtw.QWidget)
        self.my_combo.addItem("Peppers")
        self.my_combo.addItems(["One", "Two", "Three"])
        self.my_combo.insertItems(2, ["0ne","Two","Olive"])
        # Put combo box on the screen
        self.layout().addWidget(self.my_combo)

        # Create a button
        my_button = Qtw.QPushButton("Press Me!")
        my_button.clicked.connect(self.press_it)
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

    def press_it(self):
        # Add name to label
        self.my_label.setText(f'You picked {self.my_combo.currentText()}!')


if __name__ == "__main__":
    app = Qtw.QApplication([])
    mw = MainWindow()
    app.exec()