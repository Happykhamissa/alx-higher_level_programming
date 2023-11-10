#!/usr/bin/python3
"""
read_file function module.

Define read_file function.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.

        :param first_name: First name of the student.
        :param last_name: Last name of the student.
        :param age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: List of attribute names to retrieve
        :return: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
