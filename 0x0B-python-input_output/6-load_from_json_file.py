#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


import json

def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    :param filename: The name of the JSON file to load.
    :return: The Python object represented by the JSON file.
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
