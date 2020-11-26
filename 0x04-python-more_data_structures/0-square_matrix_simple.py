#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = []

    for m in range(len(matrix)):
        new_matrix.append(matrix[m].copy())
        for n in range(len(matrix[m])):
            new_matrix[m][n] = matrix[m][n]**2

    return new_matrix
