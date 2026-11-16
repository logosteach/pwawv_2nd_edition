import unittest
from grades import letter_grade

class TestNoAssert(unittest.TestCase):
    def test_grade(self):
        letter_grade(95)

if __name__ == "__main__":
    unittest.main()
