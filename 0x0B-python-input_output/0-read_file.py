#!/usr/bin/python3
"""
    0-read_file

    This module is for read a text file
"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

        Args:
            filename - the file to be read
    """
    with open(filename, encoding="utf-8") as filename:
        for line in filename:
            print(line, end='')
