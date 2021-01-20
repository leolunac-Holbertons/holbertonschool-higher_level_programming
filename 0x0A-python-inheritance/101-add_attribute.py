#!/usr/bin/python3
"""
Contains the class MyInt
"""


def add_attribute(obj, name, value):
    """
    adds attribute to an object if possible
    """
    if "__dict__" in dir(obj) and "__setattr__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
