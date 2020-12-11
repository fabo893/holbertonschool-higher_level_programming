#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    argu = len(args)
    if argu == 1:
        print("0 arguments.")
    elif argu == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argu - 1))
    for a in range(1, argu):
        print("{:d}: {:S}".format(a, args[a]))
