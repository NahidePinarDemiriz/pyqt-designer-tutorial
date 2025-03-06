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

        # Create a Text box
        self.my_text = Qtw.QTextEdit(self)
        self.my_text.setAcceptRichText(True)
        self.my_text.setText("<center><h1><b>Bold</b> ve <i>italic</i> header.<h1></center>")
        self.my_text.setLineWrapMode(Qtw.QTextEdit.LineWrapMode.FixedColumnWidth)
        self.my_text.setLineWrapColumnOrWidth(50)
        self.my_text.setPlaceholderText("Hello World!")
        self.my_text.setReadOnly(False)

        # Change font size of spin box
        #self.my_text.setFont(Qtg.QFont('Helvetica', 18))

        # Put combo box on the screen
        self.layout().addWidget(self.my_text)

        # Create a button
        my_button = Qtw.QPushButton("Press Me!")
        my_button.clicked.connect(self.press_it)
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

    def press_it(self):
        # Add name to label
        self.my_label.setText(f'You typed {self.my_text.toPlainText()}!')
        self.my_text.setPlainText("You Pressed the Button!")


if __name__ == "__main__":
    app = Qtw.QApplication([])
    mw = MainWindow()
    app.exec()