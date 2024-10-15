#!/usr/bin/python3

"""
Script that adds all arguments to a Python list and saves them to a file.
"""

from sys import argv
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file
import os

if __name__ == "__main__":
    filename = "add_item.json"

    # Check if the file exists and load existing items
    if os.path.exists(filename):
        items = load_from_json_file(filename)
    else:
        items = []

    # Add all arguments (except the script name) to the list
    items.extend(argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(items, filename)
