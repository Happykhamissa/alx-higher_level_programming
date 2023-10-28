#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.

    Args:
        my_list (list, optional): List containing elements of any type.
        x (int, optional): Number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """

    printed_integers = 0
    count = 0

    try:
        while count < x:
            try:
                print("{:d}".format(my_list[count]), end="")
                printed_integers += 1
            except (ValueError, TypeError):
                pass
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return printed_integers
