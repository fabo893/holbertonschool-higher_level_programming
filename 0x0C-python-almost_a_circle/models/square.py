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

    def update(self, *args, **kwargs):
        """Method to assign an argument to each attribute"""
        if len(args) > 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return dictionary"""
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.size
        dic['x'] = self.x
        dic['y'] = self.y
        return dic

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
