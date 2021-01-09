#!/usr/bin/python3
"""Unittest for max integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class to test a max integer in list function
    """

    def test_empty(self):
        """tests an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_positives(self):
        """tests positives in list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer(['hello', 'hello']), 'hello')
        self.assertEqual(max_integer(['a', 'b']), 'b')

    def test_negatives(self):
        """tests negatives in list
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, 0]), 0)

    def test_equals(self):
        """tests equalities in list
        """
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([2, 2]), 2)
        self.assertEqual(max_integer([-2, -2]), -2)
        self.assertEqual(max_integer([1]), 1)

    @unittest.expectedFailure
    def test_fail(self):
        """tests failure cases
        """
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(0), None)
        self.assertEqual(max_integer([0, 'a']), 'a')

if __name__ == '__main__':
    unittest.main()
