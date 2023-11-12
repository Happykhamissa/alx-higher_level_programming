class MyInt(int):
    """
    MyInt class inherits from int with inverted == and != operators.

    Attributes:
    - No additional attributes.

    Methods:
    - __eq__(self, other): Inverts the behavior of equality (==) operator.
    - __ne__(self, other): Inverts the behavior of not equal (!=) operator.
    """

    def __eq__(self, other):
        """
        Inverts the behavior of equality (==) operator.

        Args:
        - other: Another object to compare.

        Returns:
        - bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of not equal (!=) operator.

        Args:
        - other: Another object to compare.

        Returns:
        - bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)
