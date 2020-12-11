#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    from sys import argv, exit
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op == "+":
        func = add(a, b)
    elif op == "-":
        func = sub(a, b)
    elif op == "*":
        func = mul(a, b)
    elif op == "/":
        func = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, func))
