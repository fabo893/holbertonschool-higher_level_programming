#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    sec_list = my_list[:]
    if idx < 0:
        return sec_list
    else:
        sec_list[idx] = element
    return sec_list
