# author: Dabana Intenque
import main
import database
import pytest


def test_data_from_web():
    result = main.get_wufoo_data()
    for key, value in result.items():
        assert len(value) == 10


def test_new_database():
    con, cursor = database.open_database("cubes_database.db")
    database.create_database_table(cursor)
    select = cursor.execute("SELECT * from cubesProposal")
    database.create_database_table(cursor)
    my_record = cursor.fetchall()
    assert my_record == []
