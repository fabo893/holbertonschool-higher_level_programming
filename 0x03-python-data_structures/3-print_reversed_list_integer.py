#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lon = len(my_list) - 1
    if my_list is None:
        return
    for idx in my_list:
        if idx < 0:
            return
        print("{:d}".format(my_list[lon]))
        lon -= 1
