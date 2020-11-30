#!/usr/bin/python3
""" Area and Perimeter """


class Rectangle:
    """ Class Rectangle """

    def __init__(self, width=0, height=0):
        """ Instantiation width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Public instance method: area """
        return self.width * self.height

    def perimeter(self):
        """ Public instance method: perimeter """
        if self.width is 0 or self.height is 0:
            return 0
        return 2 * self.width + 2 * self.height

    def area(self):
        """ Public instance method: area """
        return self.width * self.height

    def perimeter(self):
        """ Public instance method: perimeter """
        if self.width is 0 or self.height is 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """ print the rectangle """
        if self.width is 0 or self.height is 0:
            return ''

        nl = '\n'
        return f"{('#' * self.width + nl) * self.height}"
