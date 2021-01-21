#!/usr/bin/python3
"""
function insert text after specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends new string after search string in filename
    """
    temp = ""
    with open(filename) as f:
        for line in f:
            temp += line
            if search_string in line:
                temp += new_string
    with open(filename, "w") as f:
        f.write(temp)
