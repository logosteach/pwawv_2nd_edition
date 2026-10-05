import unittest
from calculator import add


class TestFloats(unittest.TestCase):

    def test_add_decimals(self):
        # assertEqual(add(0.1, 0.2), 0.3) would FAIL!
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)


if __name__ == "__main__":
    unittest.main()
