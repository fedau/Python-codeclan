import unittest
from modules.fizzbuzz import fizzbuzz 


class FizzbuzzTest(unittest.TestCase):
    def test_num_divisible_by_3(self):
        input = 9
        expected_output = "Fizz"
        actual_output = fizzbuzz(input)
        self.assertEqual(expected_output, actual_output)
    
    def test_num_divisible_by_5(self):
        input = 10
        expected_output = "buzz"
        actual_output = fizzbuzz(input)
        self.assertEqual(expected_output, actual_output)

    def test_num_divisible_by_both(self):
        input = 15
        expected_output = "Fizzbuzz"
        actual_output = fizzbuzz(input)
        self.assertEqual(expected_output, actual_output)


    def test_none_are_divisible(self):
        input = 28
        expected_output = "28"
        actual_output = fizzbuzz(input)
        self.assertEqual(expected_output, actual_output)

