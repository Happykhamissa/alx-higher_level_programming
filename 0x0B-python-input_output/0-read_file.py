#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    :param filename: The name of the file to read.
    """
    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                print(line, end="\n")
    except FileNotFoundError:
        pass
