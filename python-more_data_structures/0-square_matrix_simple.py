#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        square = [element ** 2 for element in row]
        squared_matrix.append(square)
    return squared_matrix
