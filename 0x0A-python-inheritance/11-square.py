#!/usr/bin/python3
"""
Contains the class BaseGeometry and subclass Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from rectangle
    """
    def __init__(self, size):
        """
        instantiates square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        returns area of square
        """
        return super().area()

    def __str__(self):
        """
        string representation of square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
