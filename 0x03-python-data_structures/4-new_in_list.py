#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    sec_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return sec_list
    sec_list[idx] = element
    return sec_list
