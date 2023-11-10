#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization of an object.

    :param obj: An instance of a Class.
    :return: A dictionary representation of the object for JSON serialization.
    """
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    elif hasattr(obj, "__slots__"):
        result = {}
        if hasattr(obj, '__slots__'):
            for slot in getattr(obj, '__slots__'):
                if hasattr(obj, slot):
                    result[slot] = getattr(obj, slot)

    else:
        raise TypeError("Unsupported object type for JSON serialization")
