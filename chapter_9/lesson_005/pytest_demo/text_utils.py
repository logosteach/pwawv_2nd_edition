def is_palindrome(text):
    """Return True if text reads the same forwards and backwards.

    Ignores capital letters and spaces: "Race car" is a palindrome.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def word_count(sentence):
    """Return the number of words in a sentence."""
    return len(sentence.split())
