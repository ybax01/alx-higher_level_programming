#!/usr/bin/python3
"""
Module: 101-add_attribute
This module defines a function to add an attribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible.

    Parameters:
        obj: The object to which the attribute should be added.
        attr (str): The name of the attribute to add.
        value: The value of the attribute to add.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
