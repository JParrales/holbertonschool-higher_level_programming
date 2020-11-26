""" #!/usr/bin/python3 """


def square_matrix_simple(matrix=[]):

	new_matrix = []

	for m in range(len(matrix)):
		new_matrix.append(matrix[m].copy())		
		for n in range(len(matrix[m])):
			new_matrix[m][n] = new_matrix[m][n]**2

	return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
