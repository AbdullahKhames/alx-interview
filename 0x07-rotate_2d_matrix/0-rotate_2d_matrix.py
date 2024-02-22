#!/usr/bin/python3
"""module to solve the transpose of a matrix"""


def rotate_2d_matrix(matrix):
    """transpose a matrix"""
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > i:
                swap(matrix, i, j, j, i)


def swap(matrix, i1, j1, i2, j2):
    temp = matrix[i1][j1]
    matrix[i1][j1] = matrix[i2][j2]
    matrix[i2][j2] = temp
