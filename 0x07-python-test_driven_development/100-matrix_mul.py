#!/usr/bin/python3
"""
A function that multiplies 2 matrices:
"""


def matrix_mul(m_a, m_b):
    """
    Function for Matrix multiplication

    Raises TypeError if
        m_a or m_b is not a list or list of list.
        m_a or m_b has a non-int or non-float value's.
        m_a or m_b has a child of different length.

    Raises a ValueError if
        list or sublist is empty.
        Matrix cannot be multiplied [m_a col != m_b row]
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(num, (int, float)) for num in [val for row in m_a for val in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(num, (int, float)) for num in [val for row in m_b for val in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matA, matB = m_a, m_b
    dot_matrix = [[sum(a*b for a, b in zip(matA_row, matB_col))
                   for matB_col in zip(*matB)] for matA_row in matA]

    return dot_matrix
