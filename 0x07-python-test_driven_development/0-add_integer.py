#!/usr/bin/env python3
"""
Adding two integers

The 0-add_integer supplies one function, add_integer(a, b=98). 
It is expected to return the addition of two integer numbers.
If any of the arguments giving is neither an integer or a float,
a Typeerror is raised
For example,

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
        ...
TypeError: a must be an integer or b must be an integer

"""


def add_integer(a, b=98):
    """
    A function that adds 2 integers.

    typecast floats to ints before adding

    raised a TypeError if any arg is neither
        a float or an int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
