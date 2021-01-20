#!/usr/bin/python3
"""
writes to file
"""


def write_file(filename="", text=""):
    """
    writes string to text file, returns number of characters written
    """
    with open(filename, "w") as f:
        return f.write(str(text))
