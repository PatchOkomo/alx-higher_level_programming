#!/usr/bin/python3
"""A square with an attribute of size
defines a square with private attribute size and validates size
can access and update size
can get area
prints the square in #
"""


class Square:
    """
    Class Square definition

    Args:
    size (int): The length of the side of the square

    functions:
        __init__(self, size)
        size(self)
        size(self, value)
        area(self)
        my_print(self)
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

    @property
    def size(self):
        """"
        Getter
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter
        Args:
            value: sets size to value, if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square

        Returns:
            area
        """
        return (self.__size)**2

    def my_print(self):
        """
        Prints square using #
        """
        print("\n".join(["#" * self.__size for r in range(self.__size)]))
