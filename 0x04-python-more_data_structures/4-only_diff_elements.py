#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if len(set_1) == 0:
        set_1 = set()
    if len(set_2) == 0:
        set_2 = set()
    new = set(set_1 ^ set_2)
    return new
