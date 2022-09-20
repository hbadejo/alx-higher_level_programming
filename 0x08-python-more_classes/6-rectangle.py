#!/usr/bin/python3
"""
An empty class Rectangle that defines a rectangle
"""


class Rectangle:

    """Class Varibale def"""

    number_of_instances = 0

    """
    A class to get the size of a rectangle

    Class takes two arguments: heightand width
        of rectangle. Arguments must be of type int
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    @property
    def height(self):
        """Retrieve private instance attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """
        Set private instance attribute
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
        """
        Set private instance attribute
        Raise a TypeError if value is not int
        Raise a ValueError if value is < 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def area(self):
        """Computes the Area of rectangle"""
        return self._height * self._width

    def perimeter(self):
        """
        Returns The perimeter of the rectangle
        if any of the values turns equals 0,
        the computation equals 0
        """
        if 0 in [self._height, self._width]:
            return 0
        else:
            return 2 * (self._height + self._width)

    def __str__(self) -> str:
        """Printing format"""
        if 0 in [self._height, self._width]:
            return ""

        rect = []
        # for num in range(self.height):
        #     for val in range(self.width):
        #         print("#", end="")
        #     print("")
        for num in range(self._height):
            [rect.append("#")for val in range(self._width)]
            if num != self._height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self) -> str:
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self) -> None:
        """Print message when del is called on object"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")
