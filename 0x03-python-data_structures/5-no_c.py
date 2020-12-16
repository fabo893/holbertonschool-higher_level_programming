#!/usr/bin/python3
def no_c(my_string):
    str = my_string[:]
    str2 = ""
    for i in range(len(str)):
        if str[i] is not 'c' and str[i] is not 'C':
            str2 = str[i]
    return str2
