#!/usr/bin/python3
import json
"""
returns object represented by JSON string
"""


def to_json_string(my_obj):
    """
    returns JSON representation of an object
    """
    return json.dumps(my_obj)
