#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    sec_list = my_list[:]
    if idx < 0:
        return sec_list
    elif idx > len(my_list):
        return sec_list
    else:
        for i in my_list:
            if i == idx:
                sec_list[idx] = element
                return sec_list
