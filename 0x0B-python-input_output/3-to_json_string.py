#!/usr/bin/python3
"""
Contains the "to_json_string" fundtion
"""

import json


def to_json_string(my_obj):
    """
    returns JSON representation of an object
    """
    return json.dumps(my_obj)
