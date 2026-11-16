import unittest
from grades import letter_grade

class TestBadStyle(unittest.TestCase):
    def test_everything(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "C")
        self.assertEqual(letter_grade(72), "C")
        self.assertEqual(letter_grade(65), "D")

if __name__ == "__main__":
    unittest.main()
