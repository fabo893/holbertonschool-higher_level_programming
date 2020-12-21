#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if len(key) is not 0:
        for x in a_dictionary.keys():
            if x == key:
                del a_dictionary[key]
                return a_dictionary

    return a_dictionary
