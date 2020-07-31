#!/usr/bin/python3
"""class"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """size"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area"""
        ar = self.__size * self.__size
        return ar

    def my_print(self):
        """print"""
        if self.__size == 0:
            print()
        for a in range(self.__size):
            for b in range(self.__size):
                print("#", end="")
            print()
    pass
