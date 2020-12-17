#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    sec_list = my_list[:]
    for idx in range(0, len(my_list)):
        if my_list[idx] < 0:
            sec_list[idx] = False
        elif (my_list[idx] % 2) == 0:
            sec_list[idx] = True
        else:
            sec_list[idx] = False
    return sec_list
