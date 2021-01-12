#!/usr/bin/python3
class Rectangle:
    """
    A rectangle class
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        init method which sets the height and witdth
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        returns private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets private instance variable width with error checks
        for value error and type error
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """
        returns private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets private instance attribute height with error checks
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    def area(self):
        """
        returns the rectangle area
        """
        return self.height * self.width

    def perimeter(self):
        """
        returns the rectangle perimeter
        """
        if self.height > 0 and self.width > 0:
            return 2 * self.height + 2 * self.width
        return 0

    def __str__(self):
        """
        returns a string represntation of the rectangle built in
        the print symbol
        """
        rect = ""
        if self.height == 0 or self.width == 0:
            return rect
        for i in range(1, self.height):
            rect += str(self.print_symbol) * self.width + '\n'
        rect += str(self.print_symbol) * self.width
        return rect

    def __repr__(self):
        """
        returns a string representation of the rectangle able to be
        built with eval
        """
        return "Rectangle(" + str(self.width) + ", "\
            + str(self.height) + ")"

    def __del__(self):
        """
        prints a message when instance of rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on area
        """
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a rectangle with same size as width and height
        """
        return Rectangle(size, size)
