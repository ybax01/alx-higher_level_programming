#!/usr/bin/python3

"""
Function that returns the dictionary description for JSON serialization
of an object.
"""

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON
    serialization of an object.
    
    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary containing serializable attributes of the object.
    """
    
    return {key: value for key, value in obj.__dict__.items() 
            if isinstance(value, (list, dict, str, int, bool))}
