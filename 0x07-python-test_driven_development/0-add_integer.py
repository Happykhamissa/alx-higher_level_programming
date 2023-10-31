#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Returns:
        int: The addition of a and b as integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
