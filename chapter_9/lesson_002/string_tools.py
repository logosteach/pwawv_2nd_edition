def shout(text):
    """Return text in all caps with an exclamation point."""
    return text.upper() + "!"


def initials(full_name):
    """Return the capital first letter of each word: 'ada lovelace' -> 'AL'."""
    return "".join(word[0].upper() for word in full_name.split())


def word_list(sentence):
    """Return a list of the lowercase words in a sentence."""
    return sentence.lower().split()


def is_question(text):
    """Return True if text ends with a question mark."""
    return text.endswith("?")


def percent(part, whole):
    """Return part as a percentage of whole. Raise ValueError if whole is 0."""
    if whole == 0:
        raise ValueError("whole cannot be zero")
    return part / whole * 100
