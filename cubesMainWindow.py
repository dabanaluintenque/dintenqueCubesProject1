# author: Dabana Intenque
import sqlite3
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QMainWindow, QApplication, QTableWidget, QLabel, QPushButton, QDialog, QVBoxLayout,
                               QTableWidgetItem, QHeaderView, QWidget)

from PySide6.QtCore import Qt


class cubesWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setup()
        self.load_Data()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(5, 150)
        self.tableWidget.setHorizontalHeaderLabels(
            [" ", "Prefix", "First Name", "Last Name", "Title", "Organization Name", " Organization Website",
             "Email", "Phone Number"])

    def setup(self):
        self.setGeometry(300, 300, 1100, 500)
        self.setWindowTitle("Cubes Entries")
        self.show()

    def load_Data(self):
        self.tableWidget = QTableWidget()

        connection = sqlite3.connect("cubes_database.db")
        cur = connection.cursor()
        sqlquery = "SELECT * FROM cubesProposal"
        table_index = 0
        self.tableWidget.setRowCount(9)

        self.tableWidget.setColumnCount(9)
        for row in cur.execute(sqlquery):
            self.tableWidget.setItem(table_index, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(table_index, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(table_index, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(table_index, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(table_index, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(table_index, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.tableWidget.setItem(table_index, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.tableWidget.setItem(table_index, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.tableWidget.setItem(table_index, 8, QtWidgets.QTableWidgetItem(row[8]))
            table_index += 1


def run():
    app = QApplication(sys.argv)

    main_window = cubesWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    run()
