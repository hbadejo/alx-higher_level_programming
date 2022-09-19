#!/usr/bin/python3
"""
An empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    A class to get the size of a rectangle

    Class takes two arguments: heightand width
        of rectangle. Arguments must be of type int
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self. height = height

    @property
    def height(self):
        """Retrieve private instance attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """Retrieve private instance attribute
        Raise a TypeError if value is not int
        Raise a ValueError if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    @property
    def width(self):
        """Retrieve private instance attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Retrieve private instance attribute
        Raise a TypeError if value is not int
        Raise a ValueError if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value
