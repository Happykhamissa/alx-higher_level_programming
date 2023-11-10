#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


import json

def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
