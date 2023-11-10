#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""



def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string in a file.

    :param filename: Name of the file.
    :param search_string: String to search for in each line.
    :param new_string: String to insert after each line containing the search string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
