# from ast import main


# class Dog:
#     def __init__(self, name="", height=0, weight=0) -> None:
#         self.name = name
#         self.height = height
#         self.weight = weight

#     def run(self):
#         print("{} the dog runs".format(self.name))

#     def eat(self):
#         print("{} the dog eats".format(self.name))

#     def bark(self):
#         print("{} the dog barks".format(self.name))

#     """Defining a getter"""
#     @property
#     def name(self):
#         print("Setting name")

#         return self.__name

#     @name.setter
#     def name(self, value):
#         if value.isalpha():
#             self.__name = value
#             return self.__name
#         else:
#             raise TypeError("Value must be alpha")
#         #     self.__name = None
#         # return self.__name


# def main():
#     spot = Dog("Spot1", 66, 26)
#     spot.bark()

#     # spot1 = Dog("1", 66, 26)
#     # spot1.bark()

#     # bowser = Dog()
#     # bowser.name = "Hello"
#     # bowser.bark()


# if __name__ == "__main__":
#     main()

i = 10

[print("H") for _ in range(10)]
