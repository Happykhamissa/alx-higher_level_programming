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
        Validates the value. Raises exceptions for non-integer and non-positive values.

        Parameters:
        name (str): Name of the value.
        value: Value to be validated.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle.
    """

    def __init__(self, width, height):
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
        int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representing the rectangle.

        Returns:
        str: A string containing the rectangle's dimensions.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def print(self):
        """
        Prints the rectangle description.
        """
        print(self.__str())


class Square(Rectangle):
    """
    A class representing a Square, inheriting from Rectangle.
    """

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representing the square.

        Returns:
        str: A string containing the square's size.
        """
        return f"[Square] {self.__size}/{self.__size}"
