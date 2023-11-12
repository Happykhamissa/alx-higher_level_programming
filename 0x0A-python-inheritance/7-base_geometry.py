#!/usr/bin/python3
"""defines a class"""


class BaseGeometry:
    """
    A class representing Base Geometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value. Raises exceptions for non-integer
        and non-positive values.

        Parameters:
        name (str): Name of the value.
        value: Value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
