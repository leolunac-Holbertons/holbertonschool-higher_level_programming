#!/usr/bin/python3
"""
pascal triangle function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing
    pascals triangle
    """
    if type(n) != int:
        raise TypeError("ints only please")
    if n <= 0:
        return []
    pascal_triangle = [[1]]
    for k in range(n - 1):
        new_list = []
        a = 0
        for i in pascal_triangle[k]:
            b = i
            new_list.append(a + b)
            a = b
        new_list.append(b)
        pascal_triangle.append(new_list)
    return pascal_triangle
