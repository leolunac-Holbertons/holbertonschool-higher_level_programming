#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class which inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initialization of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overloading rectangle, str representation of square
        """
        ret_str = "[Square] ({}) {}/".format(self.id, self.x)
        return ret_str + "{} - {}".format(self.y, self.height)

    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter, uses rectangle width then height
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates attributes of square
        """
        attributes = ["id", "size", "x", "y"]
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns dictionary representation of square
        """
        ret_dict = {}
        for k, v in vars(self).items():
            if k is "id":
                ret_dict[k] = v
            elif "width" in k or "height" in k:
                ret_dict["size"] = v
            else:
                ret_dict[k[12:]] = v
        return ret_dict
