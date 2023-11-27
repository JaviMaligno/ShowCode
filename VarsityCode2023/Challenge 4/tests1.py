import unittest
from solution1 import reverse_words

class TestSolution(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_words("the quick brown fox"), "fox brown quick the")

if __name__ == '__main__':
    unittest.main()
