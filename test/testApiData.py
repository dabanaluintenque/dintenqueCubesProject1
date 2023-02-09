import main
import pytest


def test_data_from_web():
    result = main.get_wufoo_data()
    for key, value in result.items():
        assert len(value) == 10

