#!/usr/bin/python3
"""A square with an attribute of size
defines a square with private attribute size and validates size
"""


class Square:
    """
    Class Square definition

    Args:
    size (int): The length of the side of the square
    """
    def __init__(self, size=0):
        """
        Initialize a square with attribute size

        Attribute(s):
        __size (int): The length of the side of the square. Default = 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
