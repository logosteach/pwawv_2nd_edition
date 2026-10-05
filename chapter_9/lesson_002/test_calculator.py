import unittest
from calculator import add, subtract, divide, is_positive, evens_up_to


class TestCalculator(unittest.TestCase):

    def test_add_two_positives(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add(-4, 1), -3)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_gives_decimal(self):
        self.assertAlmostEqual(divide(1, 3), 0.33333, places=4)

    def test_divide_by_zero_raises_error(self):
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_is_positive_true(self):
        self.assertTrue(is_positive(7))

    def test_is_positive_false_for_negative(self):
        self.assertFalse(is_positive(-2))

    def test_evens_contains_four(self):
        self.assertIn(4, evens_up_to(10))

    def test_evens_does_not_contain_five(self):
        self.assertNotIn(5, evens_up_to(10))


if __name__ == "__main__":
    unittest.main()
