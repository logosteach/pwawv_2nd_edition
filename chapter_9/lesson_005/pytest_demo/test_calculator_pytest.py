import pytest
from calculator import add, subtract, divide, is_positive, evens_up_to


def test_add_two_positives():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_divide_gives_decimal():
    assert divide(1, 3) == pytest.approx(0.33333, abs=0.0001)


def test_is_positive():
    assert is_positive(7)


def test_is_not_positive():
    assert not is_positive(-2)


def test_evens_contains_four():
    assert 4 in evens_up_to(10)


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(5, 0)


def test_divide_by_zero_message():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(5, 0)
