#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squares = [list(map(lambda x: x**2, i))for i in matrix]
    return squares
