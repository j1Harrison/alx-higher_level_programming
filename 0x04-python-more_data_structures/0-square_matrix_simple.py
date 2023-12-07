#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	f_matrix = []
	for f in matrix:
	res = list(map(lambda x: x**2,f))
	f_matrix.append(res)
	return f_matrix
