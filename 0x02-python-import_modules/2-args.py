#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    counter = len(args)
    if counter == 1:
        print("0 arguments.")
    elif counter == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(counter - 1))
    for x in range(1, counter):
        print("{:d}: {:s}".format(x, args[x]))
