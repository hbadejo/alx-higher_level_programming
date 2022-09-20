#!/usr/bin/python3
"""
A function that prints a square with the character #.
"""


def print_square(size):
    """
    Function return a square of pounds sign
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 1:
        print("#")

    if size > 1:
        for i in range(size):
            for _ in range(size):
                print("#", end="")
            print("")
