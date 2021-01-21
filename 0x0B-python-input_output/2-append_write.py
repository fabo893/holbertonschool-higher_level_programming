#!/usr/bin/python3
"""
    2-append_write

    This module is for append text to a file
"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file

        Args:
            filename - name to the text file
            text - string to be append

        Return - the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as filename:
        filename.write(text)

    idx = 0
    for i in text:
        idx = idx + 1

    return idx
