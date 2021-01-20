#!/usr/bin/python3
"""
reads a file
"""


def read_file(filename=""):
    """
    reads a text file and prints
    """
    with open(filename) as f:
        print(f.read(), end='')
