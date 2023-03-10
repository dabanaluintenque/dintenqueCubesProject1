# author: Dabana Intenque
import sqlite3
from typing import Tuple
import get_wufoo_API_data


def open_database(name: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    database_connection = sqlite3.connect(name)

    cursor = database_connection.cursor()
    return database_connection, cursor


def close_database(connection: sqlite3.Connection):
    connection.commit()

    connection.close()


def create_database_table(cursor: sqlite3.Cursor):
    create_table = """CREATE TABLE IF NOT EXISTS teacherTable(
    entry_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    title TEXT NOT NULL,
    department TEXT NOT NULL,
    email TEXT NOT NULL,
    email TEXT NOT NULL,
    FOREIGN KEY ([entry_id]) REFERENCES [cubesProposal] ([entry_id])
  On DELETE CASCADE
    );"""

    cursor.execute(create_table)


def insert_into_cube_table(cursor: sqlite3.Cursor, entries_data: list[dict]):
    insert_data = """INSERT OR IGNORE INTO teacherTable(entry_id, first_name, last_name,
    title, department, email) VALUES(?,?,?,?,?,?)"""

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
    conn, cursor = open_database("teacher.db")
    create_database_table(cursor)
    insert_into_cube_table(cursor, entries_list)
    select = (cursor.execute("Select *From teacherTable "))
    my_record = cursor.fetchall()
    for entry in my_record:
        print(entry)
    close_database(conn)


if __name__ == '__main__':
    getData()
