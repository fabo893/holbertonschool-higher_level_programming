#!/usr/bin/python3
import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):

    def test_width(self):
        """test the width"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

if __name__ == "__main__":
    unittest.main()
