import unittest
from shapes import Rectangle


class TestRectangle(unittest.TestCase):

    def test_area(self):
        rect = Rectangle(3, 4)                # Arrange
        result = rect.area()                  # Act
        self.assertEqual(result, 12)          # Assert

    def test_perimeter(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.perimeter(), 14)

    def test_scale_changes_width_and_height(self):
        rect = Rectangle(3, 4)
        rect.scale(2)
        self.assertEqual(rect.width, 6)
        self.assertEqual(rect.height, 8)

    def test_scale_by_zero_raises(self):
        rect = Rectangle(3, 4)
        with self.assertRaises(ValueError):
            rect.scale(0)


if __name__ == "__main__":
    unittest.main()
