#!/usr/bin/python3
"""defines a class"""

class MyList(list):
    """
    MyList class inherits from the list class and provides additional methods.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
