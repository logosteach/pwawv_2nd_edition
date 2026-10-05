def fizzbuzz(n):
    """Return "Fizz" for multiples of 3, "Buzz" for multiples of 5,
    "FizzBuzz" for multiples of both, otherwise the number as a string."""
    if n < 1:
        raise ValueError("n must be 1 or greater")

    result = ""
    if n % 3 == 0:
        result += "Fizz"
    if n % 5 == 0:
        result += "Buzz"
    return result or str(n)    # empty string means "not Fizz or Buzz"
