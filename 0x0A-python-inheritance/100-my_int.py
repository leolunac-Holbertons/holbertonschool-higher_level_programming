#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """
    rebel class with reversed == and !=
    """
    def __eq__(self, other):
        """
        inverted eq method
        """
        if isinstance(other, int):
            return not super().__eq__(other)

    def __ne__(self, other):
        """
        inverted ne method
        """
        return not self.__eq__(other)
