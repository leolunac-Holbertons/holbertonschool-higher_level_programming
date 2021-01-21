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

    def to_json(self, attrs=None):
        """
        retrieves dictionary representation of Student instance
        """
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
            copy_dict = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    copy_dict[k] = v
            return copy_dict
        return self.__dict__
