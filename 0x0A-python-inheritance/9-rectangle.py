#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class with width and height
    """
    def __init__(self, width, height):
        """
        instantiation with width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
