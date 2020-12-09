#!/usr/bin/python3
for num in range(-122, -96):
    if abs(num) % 2 == 1:
            num = abs(num) - 32
    print("{}".format(chr(abs(num))), end="")
