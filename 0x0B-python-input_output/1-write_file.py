#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns the number of characters written.

    :param filename: The name of the file to write to.
    :param text: The string to write to the file.
    :return: The number of characters written.
    """
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            num_characters = file.write(text)
            return num_characters
    except FileNotFoundError:
        pass
