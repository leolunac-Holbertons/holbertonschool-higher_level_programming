#!/usr/bin/python3
"""
contains the MyList class
"""
class MyList(list):
    """
    Class that inherits from list
    """
    def print_sorted(self):
        """
        prints list in ascending sort
        """
        sort_list = super().copy()
        sort_list.sort()
        print(sort_list)