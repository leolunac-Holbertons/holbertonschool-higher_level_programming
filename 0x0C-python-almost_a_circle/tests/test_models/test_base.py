#!/usr/bin/python3
from models.base import Base
import unittest
"""
unittest for base.py
"""


class TestBase(unittest.TestCase):
    """
    test class Base for different cases
    """
    def test_empty(self):
        """
        test class in cases of no arguments
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_with_id(self):
        """
        test class with id given
        """
        b1 = Base(12)
        b2 = Base(100)
        b3 = Base(10000)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 10000)

    def test_mixed(self):
        """
        test class with mixed empty and with id
        """
        b1 = Base()
        b2 = Base(100)
        b3 = Base()
        b4 = Base(200)
        b5 = Base(0)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 100)
        self.assertEqual(b3.id, 5)
        self.assertEqual(b4.id, 200)
        self.assertEqual(b5.id, 0)

    def test_bad_input(self):
        """
        test class with unexpected inputs
        """
        b1 = Base(-1)
        self.assertEqual(b1.id, -1)
        b2 = Base(-100)
        self.assertEqual(b2.id, -100)
        b3 = Base(float("inf"))
        self.assertEqual(b3.id, float("inf"))
        b4 = Base([])
        self.assertEqual(b4.id, [])
        b5 = Base({})
        self.assertEqual(b5.id, {})
        b6 = Base((1,))
        self.assertEqual(b6.id, (1,))
        b7 = Base("Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Base(12.34)
        self.assertEqual(b8.id, 12.34)

    def test_bad_arguments(self):
        """
        test class with wrong number of arguments
        """
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)
