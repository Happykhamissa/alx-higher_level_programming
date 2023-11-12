#!/usr/bin/python3
"""defines a class"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    obj (object): The object for which attributes and methods are to be listed.

    Returns:
    list: A list of available attributes and methods of the provided object.
    """
    return [attr for attr in dir(obj)]
