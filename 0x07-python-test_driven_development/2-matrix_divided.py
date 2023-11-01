#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by div and rounded to 2 decimal places.
    """
    # Checking if the matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or not all(all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Checking if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Checking if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing each element of the matrix by div and rounding to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
