import unittest
from string_tools import shout, initials, word_list, is_question, percent


class TestStringTools(unittest.TestCase):

    def test_shout(self):
        self.assertEqual(shout("hi"), "HI!")

    def test_shout_empty_string(self):
        self.assertEqual(shout(""), "!")

    def test_initials(self):
        self.assertEqual(initials("ada lovelace"), "AL")

    def test_initials_three_names(self):
        self.assertEqual(initials("Grace Brewster Hopper"), "GBH")

    def test_word_list_contains_word(self):
        self.assertIn("python", word_list("I love Python"))

    def test_word_list_length(self):
        self.assertEqual(len(word_list("one two three")), 3)

    def test_is_question_true(self):
        self.assertTrue(is_question("Are we there yet?"))

    def test_is_question_false(self):
        self.assertFalse(is_question("We are there."))

    def test_percent(self):
        self.assertAlmostEqual(percent(1, 3), 33.333, places=2)

    def test_percent_zero_whole_raises(self):
        with self.assertRaises(ValueError):
            percent(5, 0)


if __name__ == "__main__":
    unittest.main()
