#!/usr/bin/python3
"""A square with an attribute of size
defines a square with private attribute size and validates size
can access and update size
can get area
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
    """
    def __init__(self, size=0):
        """
        Initialize a square with attribute size

        Attribute(s):
        __size (int): The length of the side of the square. Default = 0
        """
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

    def __eq__(self, other):
        """
        Compares and returns if equal
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compares and returns if not equal
        """
        return self.size != other.size

    def __lt__(self, other):
        """
        Compares and returns if lesser than
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compares and returns if lesser than or equal to
        """
        return self.size <= other.size

    def __gt__(self, other):
        """
        Compares and returns if greater than
        """
        return self.size > other.size

    def __ge__(self, other):
        """
        Compares and returns if greater than or equal to
        """
        return self.size >= other.size
