import pytest
from calculator import add, subtract, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_list_of_results():
    results = [add(1, 1), subtract(5, 2), add(2, 2)]
    assert results == [2, 3, 4]


def test_divide():
    assert divide(10, 2) == 5
