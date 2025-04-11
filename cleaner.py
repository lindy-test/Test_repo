import unittest

class TestCleaner(unittest.TestCase):
    def test_remove_nulls(self):
        self.assertEqual(remove_nulls([1, None, 2]), [1, 2])

    def test_standardize_case(self):
        self.assertEqual(standardize_case(["A", "b", None]), ["a", "b", ""])

    def test_deduplicate(self):
        self.assertEqual(deduplicate([1, 1, 2]), [1, 2])

if __name__ == '__main__':
    unittest.main()
