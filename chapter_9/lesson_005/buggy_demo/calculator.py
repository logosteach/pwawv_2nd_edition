def add(a, b):
    return a + b


def subtract(a, b):
    return b - a          # BUG: the order is backwards!


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_positive(n):
    return n > 0


def evens_up_to(n):
    return list(range(0, n + 1, 2))
