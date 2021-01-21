#!/usr/bin/python3
"""
defines a class Student
"""


class Student():
    """
    student with name and age
    """
    def __init__(self, first_name, last_name, age):
        """
        initialization
        """
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        if isinstance(first_name, str):
            self.first_name = first_name
        if isinstance(last_name, str):
            self.last_name = last_name
        if type(age) == int:
            self.age = age

    def to_json(self):
        """
        retrieves dictionary representation of Student instance
        """
        return self.__dict__
