from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 347)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.additem_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.additem_pushButton.clicked.connect(lambda : self.add_it())
        self.additem_pushButton.setGeometry(QtCore.QRect(20, 50, 111, 31))
        self.additem_pushButton.setObjectName("additem_pushButton")
        self.deleteitem_pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteitem_pushButton_2.clicked.connect(lambda: self.delete_it())
        self.deleteitem_pushButton_2.setGeometry(QtCore.QRect(130, 50, 121, 31))
        self.deleteitem_pushButton_2.setObjectName("deleteitem_pushButton_2")
        self.clearall_pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.clearall_pushButton_3.clicked.connect(lambda: self.clear_it())
        self.clearall_pushButton_3.setGeometry(QtCore.QRect(250, 50, 111, 31))
        self.clearall_pushButton_3.setObjectName("clearall_pushButton_3")
        self.additem_lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.additem_lineEdit.setGeometry(QtCore.QRect(20, 10, 341, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(20, 90, 341, 201))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add item To List
    def add_it(self):
        # Grab the item from the list box
        item = self.additem_lineEdit.text()
        # Add item to list
        self.mylist_listWidget.addItem(item)
        # Clear the item box
        self.additem_lineEdit.setText("")

    # Delete item From List
    def delete_it(self):
        # Grab the selected row or current row
        clicked = self.mylist_listWidget.currentRow()

        # Delete selected row
        self.mylist_listWidget.takeItem(clicked)

    # Clear all items From List
    def clear_it(self):
        self.mylist_listWidget.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item To List"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Delete Item From List"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Clear The List"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
