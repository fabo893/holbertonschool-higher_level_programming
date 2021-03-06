#!/usr/bin/python3
"""
This is a module documentation
"""


class Rectangle:
    """This is a rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Method __init__"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """Method that print the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((str(self.print_symbol) * self.width + '\n') *
                self.height)[0:-1]

    def __repr__(self):
        """Method __repr__"""
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.width, self.height)

    def __del__(self):
        """Method to delete"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.__class__.__name__ != "Rectangle":
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif rect_2.__class__.__name__ != "Rectangle":
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            x = rect_1.area()
            y = rect_2.area()
            if x == y:
                return rect_1
            elif x > y:
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        x = cls()
        x.width = size
        x.height = size
        return x

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
