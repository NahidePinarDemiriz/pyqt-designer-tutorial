import PyQt6.QtWidgets as Qtw
import PyQt6.QtGui as Qtg

class MainWindow(Qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("My GUI Project")

        # Set Vertical layout
        form_layout = Qtw.QFormLayout()
        self.setLayout(form_layout)

        # Add stuff/widgets
        self.label_1 = Qtw.QLabel("This is a Cool Label Row")
        self.label_1.setFont(Qtg.QFont('Helvetica', 24))
        self.f_name = Qtw.QLineEdit(self)
        self.l_name = Qtw.QLineEdit(self)

        # Create a button and connect it to the press_it method
        self.button = Qtw.QPushButton("Press me!")
        self.button.clicked.connect(self.press_it)

        # Add rows to app
        form_layout.addRow(self.label_1)
        form_layout.addRow("First Name", self.f_name)
        form_layout.addRow("Last name", self.l_name)
        form_layout.addRow(self.button)

        # Show the app
        self.show()

    def press_it(self):
        self.label_1.setText(f'You Clicked The Button, {self.f_name.text()} {self.l_name.text()} !')


if __name__ == "__main__":
    app = Qtw.QApplication([])
    mw = MainWindow()
    app.exec()