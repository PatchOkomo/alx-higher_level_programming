#!/usr/bin/python3
"""A square with an attribute of size"""


class Square:
    """represents square with size attribute"""
    def __init__(self, size):
        """
        Initialize a square with attribute size

        Args:
        size (int): The length of the side of the square
        """
        self.__size = size
