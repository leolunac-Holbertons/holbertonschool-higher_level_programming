#!/usr/bin/python3
"""
Contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Function returns True if object is instance of inherited from
    class otherwise return False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
