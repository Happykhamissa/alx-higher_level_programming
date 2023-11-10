#!/usr/bin/python3
""" Rectangle class module
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle class."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.__validate_non_negative_int("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.__validate_non_negative_int("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        self.__validate_non_negative_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        self.__validate_non_negative_int("y", value)
        self.__y = value

    def __validate_non_negative_int(self, attr_name, value):
        """Validate if value is a non-negative integer."""
        if not isinstance(value, int) or value < 0:
            raise ValueError(f"{attr_name} must be a non-negative integer")

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Display the rectangle with # characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
