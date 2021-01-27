#!/usr/bin/python3
"""
    rectangle
"""


from models.base import Base


class Rectangle(Base):
    """This class inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Method to print a string"""
        return "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id,
                self.__x, self.__y, self.__width, self.__height)

    def area(self):
        """Method that return the area"""
        return self.__width * self.__height

    def display(self):
        """Method to display the Rectangle"""
        for a in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for b in range(0, self.__x):
                print(end=" ")
            for ii in range(0, self.__width):
                print("#", end="")
            print()

    def update(self, *args):
        """Method to assign an argument to each attribute"""
        for i, j in enumerate(args):
            if i == 0:
                self.id = j
            elif i == 1:
                self.__width = j
            elif i == 2:
                self.__height = j
            elif i == 3:
                self.__x = j
            else:
                self.__y = j

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        if value > 0:
            self.__x = value
        else:
            self.__x = 0

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        if value > 0:
            self.__y = value
        else:
            self.__y = 0
