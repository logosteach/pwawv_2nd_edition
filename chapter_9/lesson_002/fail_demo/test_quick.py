import unittest
from calculator import add, subtract, divide


class TestQuick(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        # Oops: this test forgot to use assertRaises
        self.assertEqual(divide(5, 0), 0)


if __name__ == "__main__":
    unittest.main()
