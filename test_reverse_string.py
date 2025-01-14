import unittest

from reverse_string import reverse_string

class ReverseStringTests(unittest.TestCase):
    def test_with_single_letter(self):
        self.assertEqual(reverse_string("a"), "a") # add assertion here
    
    def test_with_2_letter(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_with_a_word(self):
        self.assertEqual(reverse_string("apple"), "elppa")
    
    def test_with_a_long_word(self):
        self.assertEqual(reverse_string("mississippi"), "ippississim")
    
    # def test_with_a_long_with_num(self):
        # self.assertRaises(reverse_string(1), TypeError)


if __name__ == '__main__':
    unittest.main()
