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

    # Properties and setters omitted for brevity (same as previous versions)

    def area(self):
        """
        Computes and returns the area of the Rectangle instance.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance using the `#` character to stdout,
        taking into account the `x` and `y` offsets.
        """
        # Print `y` newlines (vertical offset)
        print("\n" * self.y, end="")

        # For each row in height, print `x` spaces (horizontal offset) followed by `#` * width
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Overrides the `__str__` method to return a custom string representation
        of the Rectangle instance in the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
