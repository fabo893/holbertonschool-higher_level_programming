#!/usr/bin/python3
for x in range(-122, -96):
    if abs(x) % 2 == 1:
            x = abs(x) - 32
    print("{}".format(chr(abs(x))), end="")
