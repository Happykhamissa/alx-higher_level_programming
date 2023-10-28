#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of the division, otherwise: None.
    """

    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        try:
            print("Inside result: {}".format(result))
        except NameError:
            print("Inside result: None")
        return result
