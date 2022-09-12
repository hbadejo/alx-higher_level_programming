

"""Reading file with exception"""
# try:
#     isFile = open('data3.txt', 'r')
# except FileNotFoundError as ox:
#     print("File not found")
#     print(ox.args)
# else:
#     isRead = isFile.read()
#     print(isRead)
#     isFile.close()

"""Print Element from list with exceptions"""
# def safe_print_list(my_list=[], x=0):
#     nb_print = 0
#     for _ in range(x):
#         try:
#             print("{}".format(my_list[_]), end="")
#             nb_print = nb_print + 1
#         except IndexError:
#             break
#     print("")
#     return nb_print
# my_list = [1, 2, 3, 4, 5]
# nb_print = safe_print_list(my_list, 2)
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list))
# print("nb_print: {:d}".format(nb_print))
# nb_print = safe_print_list(my_list, len(my_list) + 2)
# print("nb_print: {:d}".format(nb_print))

"""Print an Integer"""
# def safe_print_integer(value):
#     try:
#         print("{:d}".format(value))
#         return (True)
#     except (TypeError, ValueError):
#         return (False)

"""Print and count int"""
# def safe_print_list_integers(my_list=[], x=0):
#     nb_print = 0
#     for _ in range(x):
#         try:
#             print("{:d}".format(my_list[_]), end="")
#             nb_print = nb_print + 1
#         except (TypeError, ValueError):
#             continue
#     print("")
#     return nb_print

"""Integers division with debug"""


# def safe_print_division(a, b):
#     divRes = None
#     try:
#         divRes = a / b
#     except ZeroDivisionError:
#         return None
#     finally:
#         print("Inside result: {}".format(divRes))
#         return divRes


"""Divide a list"""
# def list_division(my_list_1, my_list_2, list_length):
#     divRes = []
#     for _ in range(list_length):
#         try:
#             res = my_list_1[_] / my_list_2[_]
#         except TypeError:
#             print("wrong type")
#             res = 0
#         except ZeroDivisionError:
#             print("division by 0")
#             res = 0
#         except IndexError:
#             print("out of range")
#             res = 0
#         finally:
#             divRes.append(res)
#     return divRes

"""Function to raise exception"""
# def raise_exception():
#     raise TypeError


"""Safe integer print with error message"""




import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
