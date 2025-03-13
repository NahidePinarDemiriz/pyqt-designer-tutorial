from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sqlite3

# Create a database or connect to one
conn = sqlite3.connect("mylist.db")
# Create a cursor
c = conn.cursor()

# Create a table
c.execute(""" CREATE TABLE if not exists todo_list(
    list_item text)
    """)
# Commit the changes
conn.commit()
# Close our connection
conn.close()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 347)
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
        self.additem_lineEdit.setGeometry(QtCore.QRect(20, 10, 441, 31))
        self.additem_lineEdit.setObjectName("additem_lineEdit")
        self.mylist_listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(20, 90, 441, 201))
        self.mylist_listWidget.setObjectName("mylist_listWidget")
        self.savedb_pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.savedb_pushButton.clicked.connect(lambda: self.save_it())
        self.savedb_pushButton.setGeometry(QtCore.QRect(360, 50, 101, 31))
        self.savedb_pushButton.setObjectName("savedb_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Grab all the items from the database
        self.grab_all()
    # Grab items from database
    def grab_all(self):
        # Create a database or connect to one
        conn = sqlite3.connect("mylist.db")
        # Create a cursor
        c = conn.cursor()
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()
        # Commit the changes
        conn.commit()
        # Close our connection
        conn.close()

        # Loop through records and add to screen
        for record in records:
            self.mylist_listWidget.addItem(str(record[0]))

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

    # Save to the Database
    def save_it(self):
        # Create a database or connect to one
        conn = sqlite3.connect("mylist.db")
        # Create a cursor
        c = conn.cursor()

        # Delete everything in the database table
        c.execute('DELETE FROM todo_list;',)

        # Create blank list to hold to do list items
        items = []
        # Loop through the listWidget and pull out each item
        for index in range(self.mylist_listWidget.count()):
            items.append(self.mylist_listWidget.item(index))

        for item in items:
            #print(item.text())
            # Add stuff to the list
            c.execute("INSERT INTO todo_list VALUES (:item)",
                      {
                          'item' : item.text(),
                      })
        # Commit the changes
        conn.commit()
        # Close our connection
        conn.close()

        # Pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved To Database!!!")
        msg.setText("Your Todo List Has Been Saved!")
        msg.setIcon(QMessageBox.Icon.Information)
        x = msg.exec()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.additem_pushButton.setText(_translate("MainWindow", "Add Item To List"))
        self.deleteitem_pushButton_2.setText(_translate("MainWindow", "Delete Item From List"))
        self.clearall_pushButton_3.setText(_translate("MainWindow", "Clear The List"))
        self.savedb_pushButton.setText(_translate("MainWindow", "Save to Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
