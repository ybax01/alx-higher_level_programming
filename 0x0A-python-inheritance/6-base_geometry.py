#!/usr/bin/python3
"""
Module: 6-base_geometry
This module defines the BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    A class used as a base for geometric shapes.

    Attributes:
        None
    """

    def area(self):
        """
        Method that raises an Exception indicating that the area
        method is not implemented.

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")
