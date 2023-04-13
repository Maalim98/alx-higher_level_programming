#!/usr/bin/python3
"""this function tests if an object is an instances of a class
"""


def is_same_class(obj, a_class):
    """ this function determines if the object is
    an instance of the class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to
    """
    return type(obj) == a_class

