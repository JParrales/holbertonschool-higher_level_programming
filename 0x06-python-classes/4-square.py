#!/usr/bin/python3
""" Area of a square """


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0):
        """ initialize attribute:size  """

        self.size = size

    def area(self):
        """ Public instance method: area """

        return self.size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Public instance method: area """
        return self.__size ** 2
