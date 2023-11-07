#!/usr/bin/python3
"""defines a class"""

def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class inherited (directly or indirectly) from the specified class.

    Parameters:
    obj: Object to be checked.
    a_class: Specified class to compare against.

    Returns:
    bool: True if the object is an instance of a class inherited (directly or indirectly) from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
