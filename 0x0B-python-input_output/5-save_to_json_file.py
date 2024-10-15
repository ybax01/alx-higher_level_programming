#!/usr/bin/python3

"""
Module to write an object to a text file using a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file where the JSON will be saved.

    Returns:
        None
    """
    import json
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
