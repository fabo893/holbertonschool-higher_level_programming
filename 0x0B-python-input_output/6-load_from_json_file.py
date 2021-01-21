#!/usr/bin/python3
"""
    6-load_from_json_file

    This module is for create an object from JSON file
"""


def load_from_json_file(filename):
    """Create an object form a JSON file

        Args:
            my_obj - object
            filename - name of the text file
    """
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
