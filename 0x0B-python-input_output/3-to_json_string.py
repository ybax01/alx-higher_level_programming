#!/usr/bin/python3

"""
Module to return the JSON representation of an object (string).
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string).

    Args:
        my_obj: The object to be serialized into a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    import json
    return json.dumps(my_obj)
