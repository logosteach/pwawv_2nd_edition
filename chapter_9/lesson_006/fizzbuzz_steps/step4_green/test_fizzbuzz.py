import pytest
from fizzbuzz import fizzbuzz


def test_1_returns_string_1():
    assert fizzbuzz(1) == "1"


def test_2_returns_string_2():
    assert fizzbuzz(2) == "2"


def test_3_returns_fizz():
    assert fizzbuzz(3) == "Fizz"


def test_6_returns_fizz():
    assert fizzbuzz(6) == "Fizz"


def test_5_returns_buzz():
    assert fizzbuzz(5) == "Buzz"


def test_10_returns_buzz():
    assert fizzbuzz(10) == "Buzz"
