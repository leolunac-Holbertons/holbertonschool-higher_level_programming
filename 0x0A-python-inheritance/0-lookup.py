#!/usr/bin/python3
"""
Contains the lookup function
"""
def lookup(obj):
    """
    returns list of available attributes and methods of object
    """
    return dir(obj)
    