#!/usr/bin/python3
def common_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        set_3 = set()
        return set_3
    new = set_1 & set_2
    return new
