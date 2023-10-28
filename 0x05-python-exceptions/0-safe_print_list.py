#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list (list, optional): List containing elements of any type.
        x (int, optional): Number of elements to print. Defaults to 0.

    Returns:
        int: The real number of elements printed.
    """

    printed_elements = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            printed_elements += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_elements
