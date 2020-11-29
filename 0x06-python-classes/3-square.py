#!/usr/bin/python3
""" Area of a square """


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0):
        """ initialize attribute:size  """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def area(self):
        """ Public instance method: area """

        return self.size ** 2
