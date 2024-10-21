#!/usr/bin/python3
# models/square.py
"""
This module defines the Square class, which inherits from the Rectangle class.
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The Square class represents a square and inherits from the Rectangle class.
    
    Attributes:
        size (int): The size of the square (equivalent to width and height).
        x (int): The x-coordinate of the square.
        y (int): The y-coordinate of the square.
        id (int): The id of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The x-coordinate of the square. Default is 0.
            y (int, optional): The y-coordinate of the square. Default is 0.
            id (int, optional): The ID of the object. Default is None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter for the size attribute.
        Returns the value of the width (which is the same as height).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute. It sets both width and height to the same value.
        Uses the same validation as the Rectangle class for width.
        
        Args:
            value (int): The value to set the size (width and height) to.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the `__str__` method to return a custom string representation
        of the Square instance in the format:
        [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
