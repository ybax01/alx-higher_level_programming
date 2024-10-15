#!/usr/bin/python3

"""
Module to create an object from a JSON file.
"""


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The object represented by the JSON file.
    """
    import json
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
