import unittest
import max_integer from 6-max_integer.py 

class TestMaxInteger(unittest.TestCase):
    def test_regular_input(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_same_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([2, -3, 10, 0, -7]), 10)

    def test_float_values(self):
        self.assertEqual(max_integer([2.5, 5.7, 3.1]), 5.7)

    def test_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "orange"]), "orange")

    def test_mixed_data_types(self):
        self.assertIsNone(max_integer([5, "apple", 7.2]))  # Test case where multiple data types are present

if __name__ == '__main__':
    unittest.main()
