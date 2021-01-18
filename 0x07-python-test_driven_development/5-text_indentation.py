#!/usr/bin/python3
"""
    5-text_indentation

    This module is for indent a string
"""


def text_indentation(text):
    """Text Indentation

        Args:
            text: A string to be indented

        Return: nothing. Just print a text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    idx = 0
    for x in range(0, len(text)):
        if idx == (len(text) + 1) or idx == len(text):
            break
        if text[idx] == "." or text[idx] == "?" or text[idx] == ":":
            print(text[idx])
            print()
            if text[idx + 1] == " ":
                idx = idx + 2
            else:
                idx = idx + 1
        else:
            print(text[idx], end="")
            idx = idx + 1
