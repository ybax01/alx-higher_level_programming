#!/usr/bin/python3

"""
Student module
"""


class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to include in the
            dictionary. If None, all attributes are included.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        filtered_attrs = {attr for attr in attrs if hasattr(self, attr)}
        return {attr: getattr(self, attr) for attr in filtered_attrs}
