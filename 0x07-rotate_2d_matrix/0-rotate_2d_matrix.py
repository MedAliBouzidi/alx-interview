#!/usr/bin/python3
""" Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """
    Rotate a given matrix in-place
    Assumtions:
        - Matrix has 2 dimensions
        - Not empty
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            cell = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = cell
    for i, row in enumerate(matrix):
        matrix[i] = row[::-1]
