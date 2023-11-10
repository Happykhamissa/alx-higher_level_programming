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
        return {slot: getattr(obj, slot) for slot in obj.__slots__ if hasattr(obj, slot)}
    else:
        raise TypeError("Unsupported object type for JSON serialization")
