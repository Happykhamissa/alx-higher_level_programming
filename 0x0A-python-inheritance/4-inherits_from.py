#!/usr/bin/python3
"""defines a class"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class inherited.

    Parameters:
    obj: Object to be checked.
    a_class: Specified class to compare against.

    Returns:
    bool: True or False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
