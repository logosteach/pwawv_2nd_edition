def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_positive(n):
    return n > 0


def evens_up_to(n):
    """Return a list of the even numbers from 0 up to n (inclusive)."""
    return list(range(0, n + 1, 2))
