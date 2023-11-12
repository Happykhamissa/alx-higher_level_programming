#!/usr/bin/python3
"""defines a class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Parameters:
    obj: Object to be checked.
    a_class: Specified class to compare against.

    Returns:
    bool: True or False.
    """
    return type(obj) is a_class
