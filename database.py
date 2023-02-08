import sqlite3
from typing import Tuple


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


def insert_into_cube_table(cursor: sqlite3.Cursor):
    records = [(1, "Dr", "Dabana",
                "Jorge", "CEO",
                "Atlantic Global",
                "Atlanticglobal.com",
                "jorge@atlantic.com",
                "508-333-0000"),

               (2, "Dr", "Jhon",
                "Santore",
                "Professor",
                "BSU",
                "wwwbridgew.edu",
                "jsantore@bridgew.edu",
                "508-531-1000")
               ]
    cursor.executemany('INSERT INTO cubesProposal VALUES(?,?,?,?,?,?,?,?,?);', records)


def getDatabase():
    conn, cursor = open_database("Cubes_Database.sqlite")
    print(type(conn))
    print(type(cursor))
    create_database_table(cursor)
    insert_into_cube_table(cursor)
    close_database(conn)
