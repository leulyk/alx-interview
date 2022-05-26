#!/usr/bin/python3

"""
    Interview preparation exercise: Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """
        Function that rotates a two-dimensional square matrix
        by 90 degrees in-place
    """
    length = len(matrix[0])
    for i in range(length // 2):
        for j in range(i, length - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[length - j - 1][i]
            matrix[length - j - 1][i] = matrix[length - i - 1][length - j - 1]
            matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1]
            matrix[j][length - i - 1] = temp
