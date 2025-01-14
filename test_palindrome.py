import unittest

from palindrome import palindrome

class MyTestCase(unittest.TestCase):
    def test_single_letter(self):
        self.assertEqual(palindrome(""), True)  # add assertion here

    def test_a_word_that_is_a_palindrome(self):
        self.assertEqual(palindrome("racecar"), True)

    def test_a_word_that_is_not_a_palindrome(self):
        self.assertEqual(palindrome("hello"), False)


if __name__ == '__main__':
    unittest.main()
