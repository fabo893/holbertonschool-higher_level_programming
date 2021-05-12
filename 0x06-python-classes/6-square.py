#!/usr/bin/python3
"""6-square.py
This is a module documentation
"""


class Square:
    """This is a class documentation"""
    def __init__(self, size=0, position=(0, 0)):
        """Method __init__"""
        self.size = size
        self.position = position

    def area(self):
        """Method that return the area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            pos = self.__position
            for iii in range(0, pos[1]):
                print("\n", end="")
            for x in range(0, self.__size):
                if pos[1] < 0:
                    for xx in range(0, pos[1]):
                        print()
                else:
                    for i in range(0, pos[0]):
                        print(" ", end="")
                for ii in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position"""
        if type(value) is tuple and len(pos) is 2 and\
            type(pos[0]) is int and type(pos[1]) is int and les and les1:
                self.__position = value
        else:
            st = "position must be a tuple of 2 positive integers"
            raise TypeError(st)
