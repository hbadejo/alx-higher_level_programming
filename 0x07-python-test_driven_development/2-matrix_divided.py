#!/usr/bin/python3
"""
Function that divides all elements of a matrix
with a divisor which can be an integer or a float.
"""


def matrix_divided(matrix, div):
    """
    Function take two arg, a list of list (matrix),
    and a divider
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for item in matrix:
        if not isinstance(item, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for item in matrix:
        for val in item:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")

    for _ in range(len(matrix) - 1):
        if len(matrix[_]) > len(matrix[_ + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []

    for item in matrix:
        temp_list = []
        for val in item:
            temp_list.append(round(val / div, 2))
        new_matrix.append(temp_list)

    return new_matrix
