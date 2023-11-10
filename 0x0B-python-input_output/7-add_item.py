#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


import sys
from os.path import exists


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    :param my_obj: The object to be saved to the file.
    :param filename: The name of the file to save the object to.
    """
    import json

    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)


def load_from_json_file(filename):
    """
    Creates an object from a "JSON file".

    :param filename: The name of the JSON file to load.
    :return: The Python object represented by the JSON file.
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    # Check if the file exists, create an empty list if it doesn't
    if not exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    # Load the current list from the file
    my_list = load_from_json_file("add_item.json")

    # Add command line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list back to the file
    save_to_json_file(my_list, "add_item.json")
