#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    if len(my_list) == 0:
        return my_list
    else:
        idx = 0
        for x in new:
            if x == search:
                new[idx] = replace
            idx = idx + 1
    return new
