# If an assert is False, Python stops with an AssertionError.
# The text after the comma is the message that gets shown.
score = 85
assert score > 90, "Expected score to be greater than 90"
print("You will never see this line.")
