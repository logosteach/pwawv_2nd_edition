import pytest
from fizzbuzz import fizzbuzz


def test_1_returns_string_1():
    assert fizzbuzz(1) == "1"


def test_2_returns_string_2():
    assert fizzbuzz(2) == "2"
