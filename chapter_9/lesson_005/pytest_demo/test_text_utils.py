import pytest
from text_utils import is_palindrome, word_count


@pytest.mark.parametrize("text", ["racecar", "Racecar", "race car", "a", ""])
def test_is_palindrome_true(text):
    assert is_palindrome(text)


@pytest.mark.parametrize("text", ["python", "ab", "race cars"])
def test_is_palindrome_false(text):
    assert not is_palindrome(text)


@pytest.mark.parametrize("sentence, expected", [
    ("one two three", 3),
    ("hello", 1),
    ("", 0),
    ("  extra   spaces  here ", 3),
])
def test_word_count(sentence, expected):
    assert word_count(sentence) == expected
