import pytest
from calculator import add


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),         # two positives
    (-4, 1, -3),       # a negative
    (0, 0, 0),         # zeros
    (100, -100, 0),    # cancel out
])
def test_add(a, b, expected):
    assert add(a, b) == expected
