#!/usr/bin/python3
"""
    5-save_to_json_file

    This module is write an Object to a text fie
"""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file, using a JSON representation

        Args:
            my_obj - object
            filename - name of the text file
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
