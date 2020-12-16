#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lon = len(my_list) - 1
    if my_list is None:
        return
    else:
        for idx in my_list[::-1]:
            print("{:d}".format(my_list[idx]))
            lon -= 1
