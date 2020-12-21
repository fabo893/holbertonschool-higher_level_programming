#!/usr/bin/python3
def roman_to_int(roman_string):
    num = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100 }
    su = 0
    idx = 0
    st2 = roman_string[:]
    for st in roman_string:
        for i in num:
            if st == i:
                su += num[i]
        if idx > 0:
            if len(st2) >= 2:
                if st == 'V' and st2[idx - 1] == 'I':
                    su -= 2
            if len(st2) >= 2:
                if st == 'X' and st2[idx - 1] == 'I':
                    su -= 2
        idx += 1
    return su
