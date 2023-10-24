#!/usr/bin/python3
"""This class define a Square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size):
        """Creates new instances of square (1 side).

        Args:
            size: size of the square.
        """
        self.__size = size
