#!/usr/bin/python3
"""
function that writes object to text file with JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """
    writes object to text file using JSON representation
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
