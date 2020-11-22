#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for n in range(len(matrix[m])):
            if n < len(matrix[m]):
                print('{:d}'.format(matrix[m][n]), end=' ')
            else:
                print('{:d}'.format(matrix[m][n]), end='')

        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print_matrix_integer(matrix)