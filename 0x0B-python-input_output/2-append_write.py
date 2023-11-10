#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns the number of characters added.

    :param filename: The name of the file to append to.
    :param text: The string to append to the file.
    :return: The number of characters added.
    """
    try:
        with open(filename, mode="a", encoding="utf-8") as file:
            num_characters = file.write(text)
            return num_characters
    except FileNotFoundError:
        pass
