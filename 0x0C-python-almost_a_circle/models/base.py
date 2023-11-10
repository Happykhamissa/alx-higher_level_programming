#!/usr/bin/python3
""" Base class module
"""
import json


class Base:
    """Base class for managing id attribute in all classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
