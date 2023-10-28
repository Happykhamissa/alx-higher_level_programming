#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element from two lists and creates a new list.

    Args:
        my_list_1 (list): First list.
        my_list_2 (list): Second list.
        list_length (int): Length of the new list.

    Returns:
        list: A new list with the result of divisions or error messages.
    """

    new_list = []

    for i in range(list_length):
        try:
            result = 0
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")
            if not (isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float))):
                raise TypeError("wrong type")
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
