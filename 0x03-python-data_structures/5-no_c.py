#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for i in range(len(my_string)):
        if i is not 'c' and not 'C':
            i = my_string
    return i
