def average(numbers):
    """Return the average (mean) of a list of numbers."""
    total = 0
    for n in numbers:          # loop over EVERY number
        total += n
    return total / len(numbers)
