#!/usr/bin/python3
"""
    1-write_file

    This module is for write a string to a text file
"""


def write_file(filename="", text=""):
    """Write a string to a text file

        Args:
            filename - the name to the file
            text - the text to be write 

        Return - the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as filename:
        filename.write(text)

        idx = 0
        for i in text:
            idx = idx + 1

        return idx
