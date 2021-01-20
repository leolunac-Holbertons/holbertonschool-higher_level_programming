#!/usr/bin/python3
"""
returns number of lines in file
"""


def number_of_lines(filename=""):
    """
    returns number of lines in a text file
    """
    count = 0
    with open(filename) as f:
        for line in f:
            count += 1
    return count
