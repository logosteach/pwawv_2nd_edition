import pytest
from password import is_strong_password


def test_good_password_is_strong():
    assert is_strong_password("Secret123")

# Next: write ONE new failing test, then make it pass. Repeat.
