#!/usr/bin/python3
"""defines a class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of is a class inherited.

    Parameters:
    obj: Object to be checked.
    a_class: Specified class to compare against.

    Returns:
    bool: True or False.
    """
    return isinstance(obj, a_class)
