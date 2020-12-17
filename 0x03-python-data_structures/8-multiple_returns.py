#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tup = [0, None]
        return tup
    else:
        lon = len(sentence)
        first = sentence[0]
        tup = [lon, first]
    return tup
