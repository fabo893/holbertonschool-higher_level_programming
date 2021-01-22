#!/usr/bin/python3
"""
    1-my_list

    This module is for MyList class
"""


class MyList(list):
    """MyList class"""

    def print_sorted(self):
        """print a the list sorted"""
        print(sorted(self))
