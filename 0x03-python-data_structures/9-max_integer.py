#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        tmp = my_list[0]
        for idx in range(0, len(my_list)):
            if my_list[idx] > tmp:
                tmp = my_list[idx]
    return tmp
