import unittest
from grades import letter_grade


class TestBadStyle(unittest.TestCase):

    def test_everything(self):                    # too many behaviors in one test!
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "C")   # mistake in the TEST: should be "B"
        self.assertEqual(letter_grade(72), "C")   # never runs
        self.assertEqual(letter_grade(65), "D")   # never runs


if __name__ == "__main__":
    unittest.main()
