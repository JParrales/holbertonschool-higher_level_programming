#!/usr/bin/python3
""" Area of a square """


class Square:
    """ class Square that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiation attribute:size  """

        self.size = size
        self.position = position

    def area(self):
        """ Public instance method: area """

        return self.__size ** 2

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError(msg)
        if not all(isinstance(num, int) for num in value):
            raise TypeError(msg)
        if not all(num >= 0 for num in value):
            raise TypeError(msg)
        self.__position = value

    def my_print(self):
        """ Public instance method: my_print """

        if self.__size == 0:
            print()
            return

        print('\n' * self.__position[1], end='')
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
