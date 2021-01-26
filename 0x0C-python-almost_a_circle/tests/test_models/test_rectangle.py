#!/usr/bin/python3
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
import io
"""
unittest for Rectangle.py
"""


class TestRectangle(unittest.TestCase):
    """
    test class Rectangle for different cases
    """
    def test_stdout_display(self):
        """
        testing the display function for class
        """
        expectedString = ""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(1, 1)
        r1.display()
        expectedString += ("#" * 1 + '\n') * 1
        r2 = Rectangle(2, 3)
        r2.display()
        expectedString += ("#" * 2 + '\n') * 3
        r3 = Rectangle(3, 2)
        r3.display()
        expectedString += ("#" * 3 + '\n') * 2
        r4 = Rectangle(2, 2, 0, 1)
        r4.display()
        expectedString += ('\n') * 1 + ("#" * 2 + '\n') * 2
        r5 = Rectangle(2, 2, 1, 0)
        r5.display()
        expectedString += (" " * 1 + "#" * 2 + '\n') * 2
        r6 = Rectangle(1, 2, 2, 3)
        r6.display()
        expectedString += 3 * "\n" + (" " * 2 + "#" * 1 + '\n') * 2
        r7 = Rectangle(1, 2, 3, 2)
        r7.display()
        expectedString += ("\n" * 2) + (" " * 3 + "#" * 1 + '\n') * 2
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expectedString)

    def test_empty_id(self):
        """
        test class in cases of no arguments for id
        """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(4, 3)
        r3 = Rectangle(3, 4)
        self.assertEqual(r2.id, r1.id + 1)
        self.assertEqual(r3.id, r2.id + 1)

    def test_with_id(self):
        """
        test class with id given
        """
        r4 = Rectangle(3, 3, 0, 0, 12)
        r5 = Rectangle(1, 2, 0, 0, 100)
        r6 = Rectangle(2, 1, 0, 0, 10000)
        self.assertEqual(r4.id, 12)
        self.assertEqual(r5.id, 100)
        self.assertEqual(r6.id, 10000)

    def test_mixed_id(self):
        """
        test class with mixed empty and with id
        """
        r7 = Rectangle(1, 1)
        r8 = Rectangle(1, 1, 0, 0, 100)
        r9 = Rectangle(1, 1)
        r10 = Rectangle(1, 1, 0, 0, 200)
        r11 = Rectangle(1, 1)
        self.assertEqual(r8.id, 100)
        self.assertEqual(r9.id, r7.id + 1)
        self.assertEqual(r10.id, 200)
        self.assertEqual(r11.id, r9.id + 1)

    def test_bad_input_id(self):
        """
        test class with unexpected inputs for id
        """
        b1 = Rectangle(1, 1, 1, 1, -1)
        self.assertEqual(b1.id, -1)
        b2 = Rectangle(1, 1, 1, 1, -100)
        self.assertEqual(b2.id, -100)
        b3 = Rectangle(1, 1, 1, 1, float("inf"))
        self.assertEqual(b3.id, float("inf"))
        b4 = Rectangle(1, 1, 1, 1, [])
        self.assertEqual(b4.id, [])
        b5 = Rectangle(1, 1, 1, 1, {})
        self.assertEqual(b5.id, {})
        b6 = Rectangle(1, 1, 1, 1, (1,))
        self.assertEqual(b6.id, (1,))
        b7 = Rectangle(1, 1, 1, 1, "Hello")
        self.assertEqual(b7.id, "Hello")
        b8 = Rectangle(1, 1, 1, 1, 12.34)
        self.assertEqual(b8.id, 12.34)

    def test_bad_arguments(self):
        """
        test class with wrong number of arguments
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6)

    def test_wrong_type(self):
        """
        test class with wrong type of argument
        """
        with self.assertRaises(TypeError):
            r1 = Rectangle("str", 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "str")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "str")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, "str")
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle([], 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle({}, 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, {})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, {})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, {})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(1, "error", 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(10, 10, "error")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update("error", 10, 10, 10, "error")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(1, [1], 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(10, 10, {})
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update((1, 2), 10, 10, "error")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(10, 10, 10, 10, [])
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(1, None, 10)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(10, 10, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(None, 10, 10, 10, "error")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(10, 10, 10, None)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1)
            r1.update(10, 10, 10, 10, None)

    def test_wrong_values(self):
        """
        test class with wrong values for attributes
        """
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """
        test class for area output
        """
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.area(), 1)
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)
        r1 = Rectangle(3, 10000)
        self.assertEqual(r1.area(), 30000)

    def test_str_method(self):
        """
        tests the return of the string method
        """
        r0 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r0.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r1 = Rectangle(1, 1)
        r2 = Rectangle(5, 5, 1)
        test_str = "[Rectangle] ({}) 1/0 - 5/5".format(r1.id + 1)
        self.assertEqual(r2.__str__(), test_str)
        r3 = Rectangle(1, 1, 0, 0, "hello")
        self.assertEqual(r3.__str__(), "[Rectangle] (hello) 0/0 - 1/1")
        r4 = Rectangle(1, 1, 1, 1, {"hi": [1]})
        self.assertEqual(r4.__str__(), "[Rectangle] ({'hi': [1]}) 1/1 - 1/1")

    def test_update(self):
        """
        tests the update method of the class
        """
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(88, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (88) 10/10 - 1/10")
        r1.update(87, 2, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (87) 10/10 - 2/1")
        r1.update(86, 3, 2, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (86) 1/10 - 3/2")
        r1.update(85, 4, 3, 2, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (85) 2/1 - 4/3")
        r1.update(84, 5, 4, 3, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (84) 3/2 - 5/4")

    def test_dictionary(self):
        """
        tests to dictionary of class
        """
        r1 = Rectangle(1, 1, 0, 0, 1)
        self.d1 = {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(self.d1, r1.to_dictionary())
        r1.update(2, 2, 2, 2, 2)
        self.d2 = {'id': 2, 'width': 2, 'height': 2, 'x': 2, 'y': 2}
        self.assertDictEqual(self.d2, r1.to_dictionary())
        json_dict = Base.to_json_string(None)
        self.assertEqual("[]", json_dict)
        json_dict = Base.to_json_string([])
        self.assertEqual("[]", json_dict)
        r1_str = '[{"height": 2, "id": 2, "width": 2, "x": 2, "y": 2}]'
        json_dict = Base.to_json_string((r1.to_dictionary()))
        self.assertNotEqual(r1_str, json_dict)

    def test_json_file(self):
        """
        tests json and file io functionality
        """
        s1 = Rectangle(2, 1, 2, 2, 2)
        s2 = Rectangle(1, 2, 1, 1, 1)
        list_rectangles_input = [s1, s2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertNotEqual(list_rectangles_output[0], list_rectangles_input[0])
        self.assertNotEqual(list_rectangles_output[1], list_rectangles_input[1])
        self.assertEqual(list_rectangles_output[0].width, list_rectangles_input[0].width)
        self.assertEqual(list_rectangles_output[0].height, list_rectangles_input[0].height)
        self.assertEqual(list_rectangles_output[0].x, list_rectangles_input[0].x)
        self.assertEqual(list_rectangles_output[0].y, list_rectangles_input[0].y)