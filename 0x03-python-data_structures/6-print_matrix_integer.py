#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if n + 1 == len(matrix[m]):
                print('{:d}'.format(matrix[m][n]), end='')
            else:
                print('{:d}'.format(matrix[m][n]), end=' ')

        print()
