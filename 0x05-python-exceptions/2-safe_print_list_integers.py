#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        c = 0
        for i in range(0, x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                c = c + 1
        print()
        return c
    except (ValueError, TypeError):
        pass
