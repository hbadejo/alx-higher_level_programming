#!/usr/bin/python3

my_list = [1, 2, 3, 4, 5]

# def print_list_integer(my_list=[]):
#     for i in my_list:
#         print("{}".format(i))


# def element_at(my_list, idx):
#     if idx < 0 or idx > len(my_list) - 1:
#         return None
#     else:
#         return my_list[idx]

# def replace_in_list(my_list, idx, element):
#     if idx >= 0 or idx < len(my_list):
#         my_list[idx] = element
#     return my_list


# def print_reversed_list_integer(my_list=[]):
#     for i in range(-1, -len(my_list) - 1, -1):
#         #print(i)
#         print(my_list[i])

# def new_in_list(my_list, idx, element):
#     if idx < 0 or idx > (len(my_list) - 1):
#         return (my_list)

#     copy = [x for x in my_list]
#     copy[idx] = element
#     return (copy)
# print(new_in_list(my_list, 3, 45))
# print(my_list)

# def no_c(my_string):
#     for i in my_string:
#         if i == "c" or i == "C":
#             continue
#         print(i)
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))

# def print_matrix_integer(matrix=[[]]):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print("{:d}".format(matrix[i][j]), end="")
#             if j != (len(matrix[i]) - 1):
#                 print(" ", end="")

#         print("")


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print_matrix_integer(matrix)

# def delete_at(my_list=[], idx=0):
#     del my_list[idx]


# print(my_list)
# delete_at(my_list, 2)
# print(my_list)

a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}" .format(a, b))
