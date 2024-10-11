#!/usr/bin/python3
"""
This module provides a function add_integer that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Args:
        a: First number, must be an integer or float.
        b: Second number, must be an integer or float (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
        ValueError: If either a or b is float('nan').
        OverflowError: If float values overflow when converted to integer.
    """
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Handle float('nan') cases
    if isinstance(a, float) and (a != a):  # NaN check
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and (b != b):  # NaN check
        raise ValueError("cannot convert float NaN to integer")

    # Check for float overflow
    try:
        a = int(a)
        b = int(b)
    except OverflowError:
        raise OverflowError("float overflow occurred")

    return a + b
