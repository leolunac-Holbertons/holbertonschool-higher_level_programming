#!/usr/bin/python3
"""
This module contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    returns True if object is same as class, False otherwise
    """
    if type(obj) is a_class:
        return True
    return False
