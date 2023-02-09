import sqlite3
import sys
from typing import Tuple
from cubes_records import database_records


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
    cursor.execute('''CREATE TABLE IF NOT EXISTS cubesProposal(
    id INTEGER PRIMARY KEY,
    prefix TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT NOT NULL,
    organization_name TEXT NOT NULL,
    organization_website TEXT NOT NULL,
    email TEXT NOT NULL,
    phone_number TEXT NOT NULL
    );''')


def check_if_value_exist(cursor: sqlite3.Cursor):
    select = cursor.execute("SELECT id from cubesProposal")
    my_record = cursor.fetchall()
    for row in my_record:
        print("id", row[0])
        if row[0] == row[0]:
            print("primary key exists already")
            sys.exit(-1)
        insert_into_cube_table(cursor)


def insert_into_cube_table(cursor: sqlite3.Cursor):
    cursor.executemany('INSERT INTO cubesProposal VALUES(?,?,?,?,?,?,?,?,?);', database_records)


def getDatabase():
    conn, cursor = open_database("cubes_database.db")
    create_database_table(cursor)
    check_if_value_exist(cursor)
    insert_into_cube_table(cursor)
    close_database(conn)
