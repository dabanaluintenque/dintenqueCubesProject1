import main
import database
import pytest


def test_data_from_web():
    result = main.get_wufoo_data()
    for key, value in result.items():
        assert len(value) == 10


def test_new_database():
    con, cursor = database.open_database("create_new_empty_database")
    database.create_database_table(cursor)
    result = database.insert_into_cube_table(cursor)
    assert result is None





