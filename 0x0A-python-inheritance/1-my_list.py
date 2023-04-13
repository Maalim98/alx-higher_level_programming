#!/usr/bin/python3
"""a class which  inherts from lists"""


class MyList(list):
    """a class which  returns the sorted list for the in-built list
    """

    def print_sorted(self):
        """prints the in-built list in ascending order"""
        print(sorted(self))
