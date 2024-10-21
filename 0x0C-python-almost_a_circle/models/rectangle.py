#!/usr/bin/python3
# models/rectangle.py
"""
This module defines the Rectangle class, which inherits from the Base class.
"""

from models.base import Base

class Rectangle(Base):
    """
    The Rectangle class represents a rectangle and inherits from the Base class.
    
    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x-coordinate of the rectangle.
        __y (int): The y-coordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate. Default is 0.
            y (int, optional): The y-coordinate. Default is 0.
            id (int, optional): The ID of the object. Default is None.

        Raises:
            TypeError: If any argument is not an integer.
            ValueError: If width or height is <= 0, or x or y is < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle, with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
