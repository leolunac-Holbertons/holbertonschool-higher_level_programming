#!/usr/bin/python3
"""
This module divides elements of a matrix and will be used to test a
doctest on the function matrix_divided
"""


def matrix_divided(matrix, div):
    """
    This function divides elements of a matrix by a div number,
    raising exceptions in cases of wrong types or division by zero

    Args:
        matrix: a list of integers or floats
        div: number to divide elements of matrix with

    Returns:
        matrix: list of integers or floats divided by div
    """
    new_matrix = []
    if isinstance(matrix, list) and len(matrix) != 0:
        num_k = -1

        if type(div) != int and type(div) != float:
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division by zero')

        for i in matrix:
            temp_matrix = []

            if type(i) != list or len(i) == 0:
                raise TypeError('matrix must be a matrix (list of\
                lists) of integers/floats')

            for k in i:
                if (type(k) != int and type(k) != float):
                    raise TypeError('matrix must be a matrix (list\
                    of lists) of integers/floats')
                temp_matrix.append(round(k / div, 2))
            if num_k == -1:
                num_k = len(temp_matrix)
            if num_k != len(temp_matrix):
                raise TypeError('Each row of the matrix must have\
                the same size')
            new_matrix.append(temp_matrix)
        return new_matrix
    if len(new_matrix) == 0:
        raise TypeError('matrix must be a matrix (list of lists)\
        of integers/floats')
