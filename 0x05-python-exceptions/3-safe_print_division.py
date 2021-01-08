#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if type(a) is int and type(b) is int:
            print("Inside result: {}".format(a / b))
            return a / b
    except:
        c = None
        print("Inside result: {}".format(c))
        return c
