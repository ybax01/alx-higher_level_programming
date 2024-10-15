#!/usr/bin/python3
"""
Module to read and print the contents of a text file (UTF8).
"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.
    
    Args:
        filename (str): The name of the file to be read.
                        Defaults to an empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
