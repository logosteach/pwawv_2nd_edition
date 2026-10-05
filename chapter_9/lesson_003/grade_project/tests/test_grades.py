import unittest
from grades import letter_grade


class TestLetterGradeNormal(unittest.TestCase):
    """Normal cases: typical scores in the middle of each range."""

    def test_95_is_A(self):
        self.assertEqual(letter_grade(95), "A")

    def test_85_is_B(self):
        self.assertEqual(letter_grade(85), "B")

    def test_72_is_C(self):
        self.assertEqual(letter_grade(72), "C")

    def test_65_is_D(self):
        self.assertEqual(letter_grade(65), "D")

    def test_30_is_F(self):
        self.assertEqual(letter_grade(30), "F")


class TestLetterGradeEdges(unittest.TestCase):
    """Edge cases: right on (or just next to) a boundary."""

    def test_exactly_90_is_A(self):
        self.assertEqual(letter_grade(90), "A")

    def test_just_below_90_is_B(self):
        self.assertEqual(letter_grade(89.9), "B")

    def test_exactly_60_is_D(self):
        self.assertEqual(letter_grade(60), "D")

    def test_zero_is_F(self):
        self.assertEqual(letter_grade(0), "F")

    def test_100_is_A(self):
        self.assertEqual(letter_grade(100), "A")


class TestLetterGradeInvalid(unittest.TestCase):
    """Invalid input: the function should refuse it with an exception."""

    def test_negative_score_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_grade(-1)

    def test_score_over_100_raises_value_error(self):
        with self.assertRaises(ValueError):
            letter_grade(101)

    def test_error_message_explains_range(self):
        with self.assertRaises(ValueError) as context:
            letter_grade(150)
        self.assertIn("between 0 and 100", str(context.exception))

    def test_string_raises_type_error(self):
        with self.assertRaises(TypeError):
            letter_grade("90")

    def test_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            letter_grade(None)


if __name__ == "__main__":
    unittest.main()
