#!/usr/bin/python3
"""defines a class"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
