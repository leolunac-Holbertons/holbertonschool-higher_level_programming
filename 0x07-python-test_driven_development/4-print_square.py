#!/usr/bin/python3
"""
This module provides a square printing module to be tested using
docstring testing.
"""


def print_square(size):
    """
    Function to print a square of certain size

    Args:
        size: length of the square
    """
    if isinstance(size, int):
        if size < 0:
            raise ValueError('size must be >= 0')
        for i in range(size):
            print('#' * size)
    else:
        raise TypeError('size must be an integer')
