"""
    Implementation of Pascal's triangle
"""


def pascal_triangle(n):
    """
        Returns a list of lists of integers representing the
        Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    if n == 1:
        return triangle

    for i in range(n - 1):
        triangle.append([0 for k in range(i + 2)])
        for j in range(len(triangle[i])):
            triangle[i + 1][j] += triangle[i][j]
            triangle[i + 1][j + 1] += triangle[i][j]

    return triangle
