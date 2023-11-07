#!/usr/bin/python3
"""defines a class"""

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of, or if it's an instance of a class inherited from, the specified class.

    Parameters:
    obj: Object to be checked.
    a_class: Specified class to compare against.

    Returns:
    bool: True if the object is an instance of the specified class or inherited from it; otherwise False.
    """
    return isinstance(obj, a_class)
