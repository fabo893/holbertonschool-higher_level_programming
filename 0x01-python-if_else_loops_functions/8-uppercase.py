#!/usr/bin/python3
def uppercase(str):
    for x in str:
        let = ord(x)
        if x.islower():
            let -= 32
        print("{:c}".format(let), end="")
    print()
