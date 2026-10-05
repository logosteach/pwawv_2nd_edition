import unittest


class TestLifecycle(unittest.TestCase):

    def setUp(self):
        print("  setUp: build a fresh object")

    def tearDown(self):
        print("  tearDown: clean up")

    def test_first(self):
        print("  running test_first")

    def test_second(self):
        print("  running test_second")


if __name__ == "__main__":
    unittest.main()
