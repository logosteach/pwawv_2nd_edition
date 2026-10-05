import unittest


class TestNaming(unittest.TestCase):

    def test_this_one_runs(self):
        self.assertEqual(1 + 1, 2)

    def check_this_one_is_skipped(self):    # does NOT start with "test"
        self.assertEqual(1 + 1, 3)          # would fail... but never runs


if __name__ == "__main__":
    unittest.main()
