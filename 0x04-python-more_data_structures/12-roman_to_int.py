#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    su = 0
    idx = 0
    if type(roman_string) is not str or roman_string is None:
        return 0
    st2 = roman_string[:]
    for st in roman_string:
        for i in num:
            if st == i:
                su += num[i]
        if idx > 0:
            if st2[idx] == 'V' and st2[idx - 1] == 'I':
                su -= 2
            if st2[idx] == 'X' and st2[idx - 1] == 'I':
                su -= 2
            if st2[idx] == 'L' and st2[idx - 1] == 'X':
                su -= 10
            if st2[idx] == 'C' and st2[idx - 1] == 'X':
                su -= 10
            if st2[idx] == 'D' and st2[idx - 1] == 'C':
                su -= 100
            if st2[idx] == 'M' and st2[idx - 1] == 'C':
                su -= 100
        idx += 1
    return su
