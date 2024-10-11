#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats casted as integers.
    
    Args:
        a: The first number, can be an integer or float.
        b: The second number, default is 98, can be an integer or float.
        
    Returns:
        The sum of a and b as an integer.
    
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
