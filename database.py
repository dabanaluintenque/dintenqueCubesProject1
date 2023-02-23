# author: Dabana Intenque
import sqlite3
import sys
from typing import Tuple

from PySide6 import QtWidgets

import get_wufoo_API_data
from cubes_records import database_records
# author: Dabana Intenque
import sys

from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QTableWidget
from buttons import close_window_button


# Bringing all the widgets and vents needed to build the application from pyside6 Library

# Opening the Database
def open_database(name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    # connect to existing DB or create new one
    database_connection = sqlite3.connect(name)
    # creating cursor object
    cursor = database_connection.cursor()
    return database_connection, cursor


# Closing the Database
def close_database(connection: sqlite3.Connection):
    # saving the changes before closing the database
    connection.commit()
    # then close Database
    connection.close()


def create_database_table(cursor: sqlite3.Cursor):
    create_table = """CREATE TABLE IF NOT EXISTS cubesProposal(
    entry_id INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT NOT NULL,
    organization_name TEXT NOT NULL,
    organization_website TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL
    );"""

    cursor.execute(create_table)


def insert_into_cube_table(cursor: sqlite3.Cursor, entries_data: list[dict]):
    # insert if the primary key don't exist otherwise Ignore
    insert_data = """INSERT OR IGNORE INTO cubesProposal(entry_id, prefix, first_name, last_name,
    title, organization_name, organization_website, email, phone_number) VALUES(?,?,?,?,?,?,?,?,?)"""

    for entry in entries_data:
        entry_values = list(
            entry.values()
        )
        entry_values[0] = int(
            entry_values[0]
        )
        entry_values = entry_values[:-16]
        cursor.execute(insert_data, entry_values)


def getData():
    json_response = get_wufoo_API_data.get_wufoo_data()
    entries_list = json_response["Entries"]
    conn, cursor = open_database("cubes_database.db")
    create_database_table(cursor)
    insert_into_cube_table(cursor, entries_list)
    select = (cursor.execute("Select *From cubesProposal "))
    my_record = cursor.fetchall()
    for entry in my_record:
        print(entry)
    close_database(conn)
