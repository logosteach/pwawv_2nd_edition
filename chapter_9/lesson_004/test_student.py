import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.student = Student("Sam", 10)

    # 1. Starting state
    def test_new_student_name_and_grade(self):
        self.assertEqual(self.student.name, "Sam")
        self.assertEqual(self.student.grade_level, 10)

    def test_new_student_has_no_scores(self):
        self.assertEqual(self.student.scores, [])

    def test_invalid_grade_level_raises(self):
        with self.assertRaises(ValueError):
            Student("Kim", 8)

    # 2. add_score
    def test_add_score_stores_score(self):
        self.student.add_score(88)
        self.assertIn(88, self.student.scores)

    def test_add_score_over_100_raises(self):
        with self.assertRaises(ValueError):
            self.student.add_score(101)

    def test_bad_score_is_not_stored(self):
        with self.assertRaises(ValueError):
            self.student.add_score(-5)
        self.assertEqual(self.student.scores, [])

    # 3. average
    def test_average_with_no_scores_is_zero(self):
        self.assertEqual(self.student.average(), 0.0)

    def test_average_of_three_scores(self):
        for score in [80, 90, 75]:
            self.student.add_score(score)
        self.assertAlmostEqual(self.student.average(), 81.6667, places=3)

    # 4. highest
    def test_highest_with_no_scores_is_none(self):
        self.assertIsNone(self.student.highest())

    def test_highest_score(self):
        for score in [70, 99, 85]:
            self.student.add_score(score)
        self.assertEqual(self.student.highest(), 99)

    # 5. is_passing
    def test_passing_at_exactly_60(self):
        self.student.add_score(60)
        self.assertTrue(self.student.is_passing())

    def test_not_passing_below_60(self):
        self.student.add_score(59)
        self.assertFalse(self.student.is_passing())

    # 6. promote
    def test_promote_increases_grade_level(self):
        self.student.promote()
        self.assertEqual(self.student.grade_level, 11)

    def test_senior_cannot_be_promoted(self):
        senior = Student("Lee", 12)
        with self.assertRaises(ValueError):
            senior.promote()


if __name__ == "__main__":
    unittest.main()
