#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Inherits from base, rectangle class with width and height
    and corresponding getters/setters
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """
        returns area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout a Rectangle instance with character '#'
        """
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """
        str magic method returning the rectangle and attributes
        """
        ret_str = "[Rectangle] (" + str(self.id) + ") " + str(self.x)
        ret_str += "/" + str(self.y) + " - " + str(self.width) + "/"
        return ret_str + str(self.height)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) is not 0:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs is not None:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        returns dictionary representation of rectangle
        """
        ret_dict = {}
        for k, v in vars(self).items():
            if k is not "id":
                ret_dict[k[12:]] = v
            else:
                ret_dict[k] = v
        return ret_dict
