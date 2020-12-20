#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = []
    if len(a_dictionary) == 0:
        return
    else:
        for x in a_dictionary.items():
            new.append(x)

        new.sort()

        for x in new:
            print("{}: {}".format(x[0], x[1]))
