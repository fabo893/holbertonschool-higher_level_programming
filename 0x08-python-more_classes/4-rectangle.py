#!/usr/bin/python3
"""
This is a module documentation
"""


class Rectangle:
    """Method __init__"""
    def __init__(self, width=0, height=0):
        """Method __init__"""
        self.width = width
        self.height = height

    def __str__(self):
        """Method that print the rectangle"""
        if self.area == 0:
            return ""
        return (('#' * self.width + '\n') * self.height)[0:-1]

    def __repr__(self):
        """Method __repr__"""
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.width, self.height)

    def area(self):
        """Method that return the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that return the perimeter"""
        if int(self.__width) == 0:
            return 0
        elif int(self.__height) == 0:
            return 0
        else:
            x = self.__width * 2
            y = self.__height * 2
            return x + y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
