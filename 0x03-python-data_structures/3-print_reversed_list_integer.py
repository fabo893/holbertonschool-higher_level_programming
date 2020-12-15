#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    lon = len(my_list) - 1
    for idx in my_list:
        print("{:d}".format(my_list[lon]))
        lon -= 1
