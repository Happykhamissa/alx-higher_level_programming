#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON-formatted string.
    :return: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
