from buggy_average import average

# Automated tests: each line states what SHOULD be true.
assert average([0, 4, 8]) == 4, "average([0, 4, 8]) should be 4"
assert average([2, 4, 6]) == 4, "average([2, 4, 6]) should be 4"
assert average([10]) == 10, "average([10]) should be 10"

print("All tests passed!")
