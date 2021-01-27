#!/usr/bin/python3
"""
    test_base
"""


import unittest
from models import base

Base = base.Base


class TestBase(unittest.TestCase):
    """For check Base class"""

    def test_id(self):
        """id is None"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_again_id(self):
        """id has int"""
        b2 = Base(12)
        self.assertEqual(b2.id, 12)

    def test_float_id(self):
        """id has float"""
        b3 = Base(3.14)
        self.assertEqual(b3.id, 2)

    def test_str_id(self):
        """id has string"""
        b4 = Base("hey")
        self.assertEqual(b4.id, 3)

if __name__ == "__main__":
    unittest.main()
