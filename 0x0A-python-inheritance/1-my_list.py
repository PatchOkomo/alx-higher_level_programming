#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
