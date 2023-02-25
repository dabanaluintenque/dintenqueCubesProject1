# author: Dabana Intenque
import sqlite3

import Cubes_GUI
import database


def test_selected_data():
    method_to_test = Cubes_GUI.selected_items
    assert Cubes_GUI.Guest_Speaker_check_box != False
    assert Cubes_GUI.Internships_check_box != True
    assert Cubes_GUI.first_name_box == Cubes_GUI.first_name_box
    assert (Cubes_GUI.last_name_box != '')
    assert (Cubes_GUI.phone_number_box != '')


def test_check_if_there_is_data_in_table():
    c = Cubes_GUI.con
    cursor = c.cursor()
    select = cursor.execute("SELECT * from cubesProposal where prefix=2")
    my_record = cursor.fetchall()
    assert my_record != ''
