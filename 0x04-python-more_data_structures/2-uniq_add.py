#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    res = 0
    if len(my_list) == 0:
        return 0
    else:
        for x in new:
            res = res + x
    return res
