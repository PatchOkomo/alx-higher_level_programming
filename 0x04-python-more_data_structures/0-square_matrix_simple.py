#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """j is the row of the matrix"""
    return ([list(map(lambda i: i * i, j)) for j in matrix])
