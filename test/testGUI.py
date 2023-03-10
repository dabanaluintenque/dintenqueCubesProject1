# author: Dabana Intenque
import sqlite3

import backend_functions
import cubes_window
import database


def test_selected_data():
    method_to_test = cubes_window.selected_items


def test_check_if_there_is_data_in_table():
    c = backend_functions.con
    cursor = c.cursor()
    select = cursor.execute("SELECT * from cubesProposal where prefix=2")
    my_record = cursor.fetchall()
    assert my_record != ''
