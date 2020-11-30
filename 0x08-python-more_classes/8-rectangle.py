#!/usr/bin/python3
""" Change representation """


class Rectangle:
    """ Class Rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangl """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """ print the rectangle """
        if self.width is 0 or self.height is 0:
            return ''

        return '{}{}'.format(
                (str(self.print_symbol) * self.width +
                    '\n') * (self.height - 1),
                str(self.print_symbol) * self.width
            )

    def __repr__(self):
        """ Representation of rectangle """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """Delete Instance rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
