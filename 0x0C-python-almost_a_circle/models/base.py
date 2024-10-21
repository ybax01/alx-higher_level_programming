#!/usr/bin/python3
# models/base.py
"""
This module defines the Base class,
which will serve as the base for other classes in this project.
"""


class Base:
    """
    The Base class to manage 'id' attribute in all future derived classes.

    Attributes:
        __nb_objects (int): Private class attribute
        to keep track of the number of objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int, optional): If provided, it is assigned to the instance.
            Otherwise, increment __nb_objects and assign the new value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
