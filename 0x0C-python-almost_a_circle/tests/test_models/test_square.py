#!/usr/bin/python3
from models.square import Square
from models.base import Base
import io
import sys
import unittest
"""
unittest for Square.py
"""


class TestSquare(unittest.TestCase):
    """
    test class Square for different cases
    """
    def test_stdout_display(self):
        """
        testing the display function for class
        """
        expectedString = ""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        s1 = Square(1)
        s1.display()
        expectedString += ("#" * 1 + '\n') * 1
        r2 = Square(2)
        r2.display()
        expectedString += ("#" * 2 + '\n') * 2
        r3 = Square(3)
        r3.display()
        expectedString += ("#" * 3 + '\n') * 3
        r4 = Square(2, 0, 1)
        r4.display()
        expectedString += ('\n') * 1 + ("#" * 2 + '\n') * 2
        r5 = Square(2, 1, 0)
        r5.display()
        expectedString += (" " * 1 + "#" * 2 + '\n') * 2
        r6 = Square(2, 2, 3)
        r6.display()
        expectedString += 3 * "\n" + (" " * 2 + "#" * 2 + '\n') * 2
        r7 = Square(2, 3, 2)
        r7.display()
        expectedString += ("\n" * 2) + (" " * 3 + "#" * 2 + '\n') * 2
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expectedString)

    def test_empty_id(self):
        """
        test class in cases of no arguments
        """
        s1 = Square(1)
        s2 = Square(2)
        s3 = Square(3)
        self.assertEqual(s2.id, s1.id + 1)
        self.assertEqual(s3.id, s2.id + 1)

    def test_with_id(self):
        """
        test class with id given
        """
        s1 = Square(1, 1, 1, 12)
        s2 = Square(1, 1, 1, 100)
        s3 = Square(1, 1, 1, 10000)
        self.assertEqual(s1.id, 12)
        self.assertEqual(s2.id, 100)
        self.assertEqual(s3.id, 10000)

    def test_mixed(self):
        """
        test class with mixed empty and with id
        """
        s1 = Square(1)
        s2 = Square(1, 1, 1, 100)
        s3 = Square(1)
        s4 = Square(1, 1, 1, 200)
        s5 = Square(1, 1, 1, 0)
        self.assertEqual(s2.id, 100)
        self.assertEqual(s3.id, s1.id + 1)
        self.assertEqual(s4.id, 200)
        self.assertEqual(s5.id, 0)

    def test_bad_input_id(self):
        """
        test class with unexpected inputs
        """
        s1 = Square(1, 1, 1, -1)
        self.assertEqual(s1.id, -1)
        b2 = Square(1, 1, 1, -100)
        self.assertEqual(b2.id, -100)
        b3 = Square(1, 1, 1, float("inf"))
        self.assertEqual(b3.id, float("inf"))
        b4 = Square(1, 1, 1, [])
        self.assertEqual(b4.id, [])
        b5 = Square(1, 1, 1, {})
        self.assertEqual(b5.id, {})
        b6 = Square(1, 1, 1, (1,))
        self.assertEqual(b6.id, (1,))
        b7 = Square(1, 1, 1, "Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Square(1, 1, 1, 12.34)
        self.assertEqual(b8.id, 12.34)

    def test_bad_arguments(self):
        """
        test class with wrong number of arguments
        """
        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)

    def test_wrong_type(self):
        """
        test class with wrong type of argument
        """
        with self.assertRaises(TypeError):
            s1 = Square("str", 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, "str")
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, "str")
        with self.assertRaises(TypeError):
            s1 = Square(None, 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, None)
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, None)
        with self.assertRaises(TypeError):
            s1 = Square([], 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, [])
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, [])
        with self.assertRaises(TypeError):
            s1 = Square({}, 1)
        with self.assertRaises(TypeError):
            s1 = Square(1, {})
        with self.assertRaises(TypeError):
            s1 = Square(1, 1, {})
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(1, "error", 10)
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(10, 10, "error")
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update("error", 10, 10, "error")
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(1, [1], 10)
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(10, 10, {})
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update((1, 2), 10, 10, "error")
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(1, None, 10)
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(10, 10, None)
        with self.assertRaises(TypeError):
            s1 = Square(1, 1)
            s1.update(None, 10, 10, "error")

    def test_wrong_values(self):
        with self.assertRaises(ValueError):
            s1 = Square(0)
        with self.assertRaises(ValueError):
            s1 = Square(-1)
        with self.assertRaises(ValueError):
            s1 = Square(1, 1)
            s1.update(1, 0)
        with self.assertRaises(ValueError):
            s1 = Square(1, 1)
            s1.update(1, 0)

    def test_area(self):
        """
        test class for area output
        """
        s1 = Square(1)
        self.assertEqual(s1.area(), 1)
        s1 = Square(2)
        self.assertEqual(s1.area(), 4)
        s1 = Square(10000)
        self.assertEqual(s1.area(), 100000000)

    def test_str_method(self):
        """
        tests the return of the string method
        """
        r0 = Square(4, 2, 1, 12)
        self.assertEqual(r0.__str__(), "[Square] (12) 2/1 - 4")
        s1 = Square(1, 1)
        r2 = Square(5, 1)
        test_str = "[Square] ({}) 1/0 - 5".format(s1.id + 1)
        self.assertEqual(r2.__str__(), test_str)
        r3 = Square(1, 0, 0, "hello")
        self.assertEqual(r3.__str__(), "[Square] (hello) 0/0 - 1")
        r4 = Square(1, 1, 1, {"hi": [1]})
        self.assertEqual(r4.__str__(), "[Square] ({'hi': [1]}) 1/1 - 1")

    def test_update(self):
        """
        tests the update method of the class
        """
        s1 = Square(10, 10, 10, 1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(89)
        self.assertEqual(s1.__str__(), "[Square] (89) 10/10 - 10")
        s1.update(88, 1)
        self.assertEqual(s1.__str__(), "[Square] (88) 10/10 - 1")
        s1.update(87, 2, 1)
        self.assertEqual(s1.__str__(), "[Square] (87) 1/10 - 2")
        s1.update(86, 3, 2, 1)
        self.assertEqual(s1.__str__(), "[Square] (86) 2/1 - 3")
        s1.update(85, 4, 3, 2)
        self.assertEqual(s1.__str__(), "[Square] (85) 3/2 - 4")
        s1 = Square(10, 10, 10, "hi")
        self.assertEqual(s1.__str__(), "[Square] (hi) 10/10 - 10")
        s1 = Square(10, 10, 10, [1, 2])
        self.assertEqual(s1.__str__(), "[Square] ([1, 2]) 10/10 - 10")

    def test_dictionary(self):
        """
        tests to dictionary of class
        """
        r1 = Square(1, 0, 0, 1)
        self.d1 = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(self.d1, r1.to_dictionary())
        r1.update(2, 2, 2, 2)
        self.d2 = {'id': 2, 'size': 2, 'x': 2, 'y': 2}
        self.assertDictEqual(self.d2, r1.to_dictionary())
        json_dict = Base.to_json_string(None)
        self.assertEqual("[]", json_dict)
        json_dict = Base.to_json_string([])
        self.assertEqual("[]", json_dict)

    def test_json_file(self):
        """
        tests json and file io functionality
        """
        s1 = Square(2, 2, 2, 2)
        s2 = Square(1, 1, 1, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertNotEqual(list_squares_output[0], list_squares_input[0])
        self.assertNotEqual(list_squares_output[1], list_squares_input[1])
        self.assertEqual(list_squares_output[0].size, list_squares_input[0].size)
        self.assertEqual(list_squares_output[0].x, list_squares_input[0].x)
        self.assertEqual(list_squares_output[0].y, list_squares_input[0].y)
