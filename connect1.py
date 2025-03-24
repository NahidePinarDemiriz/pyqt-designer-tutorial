from PyQt6 import QtCore, QtGui, QtWidgets
from connect2 import Ui_SecondWindow

class Ui_Dialog(object):
    def open_window(self):
        # Open second window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def clicker(self):
        thing = self.lineEdit.text()
        # Assign thing to second window label
        self.ui.label.setText(thing)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(304, 306)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.clicked.connect(lambda: self.clicker())
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 281, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.clicked.connect(lambda: self.open_window())
        self.pushButton_2.setGeometry(QtCore.QRect(10, 240, 281, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 281, 141))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Open Window"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
