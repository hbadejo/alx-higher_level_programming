#!/usr/bin/python3

# --------question 0

# class Square:
#     pass


# --------question 1

# class Square:

#     def __init__(self, size) -> None:
#         self.__size = size

# ------question 2

# class Square:

#     def __init__(self, size=0) -> None:
#         if not isinstance(size, int):
#             raise TypeError("size must be an integer")
#         elif size < 0:
#             raise ValueError("size must be >= 0")
#         else:
#             self.__size = size

# ------question 3

# class Square:

#     def __init__(self, size=0) -> None:
#         if not isinstance(size, int):
#             raise TypeError("size must be an integer")
#         elif size < 0:
#             raise ValueError("size must be >= 0")
#         else:
#             self.__size = size

#     def area(self):
#         return (self.__size**2)


# ------question 4

# class Square:

#     def __init__(self, size=0) -> None:
#         self.__size = size

#     def area(self):
#         return (self.__size**2)

#     @property
#     def size(self):
#         return self.__size

#     @size.setter
#     def size(self, value):
#         if not isinstance(value, int):
#             raise TypeError("size must be an integer")
#         elif value < 0:
#             raise ValueError("size must be >= 0")
#         else:
#             self.__size = value
#         return self.__size


# ------question 5
# class Square:

#     def __init__(self, size=0) -> None:
#         self.__size = size

#     def area(self):
#         return (self.__size**2)

#     @property
#     def size(self):
#         return self.__size

#     @size.setter
#     def size(self, value):
#         if not isinstance(value, int):
#             raise TypeError("size must be an integer")
#         elif value < 0:
#             raise ValueError("size must be >= 0")
#         else:
#             self.__size = value
#         return self.__size

#     def my_print(self):
#         view = "#"
#         if self.__size is 0:
#             print("")
#         else:
#             for i in range(self.__size):
#                 for j in range(self.__size):
#                     print(view, end="")
#                 print("")


# ------question 6


from turtle import position


class Square:

    def __init__(self, size=0, position=(0, 0)) -> None:
        self.size = size
        self.position = position

    def area(self):
        return (self.__size**2)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        [print("") for _ in range(self.position[1])]
        for i in range(self.__size):
            [print(" ", end="") for _ in range(self.position[0])]
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

# ------question 100
