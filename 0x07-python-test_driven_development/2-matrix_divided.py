#!/usr/bin/python3
"""
Task: 1. Divide a matrix
Function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    if (type(matrix) is not list or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    out = map(lambda x: list(map(lambda y: round(y / div, 2), x)), ma0trix)

    return list(out)
