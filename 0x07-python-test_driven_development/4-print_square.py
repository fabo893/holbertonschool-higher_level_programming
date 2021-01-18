#!/usr/bin/python3
"""
    4-print_square

    This module is for print a square
"""


def print_square(size):
    """Print a square

        Args:
            size: the length of the square

        Return: nothing but a printed square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and float(size) < 0:
        raise TypeError("size must be an integer")

    for x in range(0, size):
        for i in range(0, size):
            print("#", end="")
        print()
