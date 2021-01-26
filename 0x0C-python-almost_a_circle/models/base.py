#!/usr/bin/python3
"""
base module
"""
import json


class Base:
    """
    Class that makes the base for other classes.
    Manages __nb_objects and public instance attribute id.
    """
    __nb_object = 0

    def __init__(self, id=None):
        """
        initialize with given id or if None increment __nb_objects
        and assign new value to id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation to list_objs file
        """
        name = cls.__name__ + ".json"
        ret_list = []
        if list_objs is not None:
            for i in list_objs:
                ret_list.append(i.to_dictionary())
        with open(name, 'w') as f:
            f.write(cls.to_json_string(ret_list))

    @staticmethod
    def from_json_string(json_string):
        """
        returns list of JSON string representation
        """
        if json_string is None or json_string is "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns instance with attributes already set
        """
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        retuns list of instances
        """
        name = cls.__name__ + ".json"
        ret_list = []
        with open(name) as f:
            file_list = cls.from_json_string(f.read())
        for i in file_list:
            n = cls.create(**i)
            ret_list.append(n)
        return ret_list
