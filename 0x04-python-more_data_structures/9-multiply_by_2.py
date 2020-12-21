#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if len(a_dictionary) == 0:
        tmp = {}
        return 0
    else:
        tmp = {}
        for x in a_dictionary:
            num = 0
            num = (a_dictionary[x] * 2)
            tmp[x] = num
    return tmp
