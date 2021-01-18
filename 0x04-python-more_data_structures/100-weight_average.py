#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0
    else:
        res = 0
        div = 0
        for x in my_list:
            res = res + (x[0] * x[1])
            div = div + x[1]
        return res / div
