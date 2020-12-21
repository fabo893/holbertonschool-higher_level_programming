#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        score = 0
        idx = 0
        name = list()
        for i in a_dictionary:
            if score < a_dictionary[i]:
                score = a_dictionary[i]
                name.append(i)
            idx = idx + 1
    return name[-1]
