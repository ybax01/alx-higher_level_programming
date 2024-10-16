#!/usr/bin/python3
class MyList(list):
    """
    A subclass of the built-in list class
    with an additional method to print the list in sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order without modifying the original list.
        """
        print(sorted(self))
