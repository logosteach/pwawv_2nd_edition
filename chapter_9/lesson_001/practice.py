# Lesson 1 Practice: one of these functions works, two have bugs.
# Write assert statements to find out which!


def is_even(n):
    """Return True if n is even, otherwise False."""
    return n % 2 == 0


def max_of_three(a, b, c):
    """Return the largest of three numbers."""
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def count_vowels(word):
    """Return how many vowels (a, e, i, o, u) are in word, upper or lower case."""
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count
