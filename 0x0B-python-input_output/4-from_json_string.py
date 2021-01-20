#!/usr/bin/python3
import json
"""
returns object represented by JSON string
"""


def from_json_string(my_str):
    """
    returns object represented by JSON string
    """
    return json.loads(my_str)
