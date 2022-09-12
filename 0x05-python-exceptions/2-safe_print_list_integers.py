#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    for _ in range(x):
        try:
            print("{:d}".format(my_list[_]), end="")
            nb_print = nb_print + 1
        except (TypeError, ValueError):
            continue
    print("")
    return nb_print
