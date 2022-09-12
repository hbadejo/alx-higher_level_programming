#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divRes = a / b
    except ZeroDivisionError:
        divRes = None
    finally:
        print("Inside result: {}".format(divRes))
        return divRes
