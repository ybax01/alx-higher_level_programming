#!/usr/bin/python3
"""
Module: 100-my_int
This module defines the MyInt class that inverts the == and != operators.
"""


class MyInt(int):
    """
    A class that inherits from int and inverts the behavior of == and !=.
    """

    def __eq__(self, other):
        """Inverts the equality comparison."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the inequality comparison."""
        return super().__eq__(other)
