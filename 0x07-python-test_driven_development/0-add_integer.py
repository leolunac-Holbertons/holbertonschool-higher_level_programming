#!/usr/bin/python3
"""
This module provides an integer add function to be tested using
docstring testing.
"""


def add_integer(a, b=98):
    """
    Function to add two integers, error if non integers or floats

    Args:
        a: first integer to add
        b: second integer to add

    Returns:
        a + b (int): sum of a and b
    """
    if type(a) == float or type(a) == int:
        a = int(a)
    else:
        raise TypeError('a must be an integer')

    if type(b) == float or type(b) == int:
        b = int(b)
    else:
        raise TypeError('b must be an integer')

    return a + b
