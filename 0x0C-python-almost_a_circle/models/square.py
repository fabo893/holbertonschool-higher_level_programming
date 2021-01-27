#!/usr/bin/python3
"""
    square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class inherits from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Method to print a string"""
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x,
                self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
