import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("n, expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (6, "Fizz"),
    (5, "Buzz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected


@pytest.mark.parametrize("bad", [0, -3])
def test_numbers_below_1_raise_value_error(bad):
    with pytest.raises(ValueError):
        fizzbuzz(bad)
