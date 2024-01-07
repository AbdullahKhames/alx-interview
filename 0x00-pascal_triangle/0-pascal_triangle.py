#!/usr/bin/python3
"""
pascal triangle definintion
"""


def pascal_triangle(n):
    """pascal triangle method to solve

    Args:
        n (int): number of rows in 
    """
    if n <= 0:
        return []
    if type(n) is not int:
        raise TypeError("n must be a positive integer")
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            triangle.append([])
            for j in range(i + 1):
                if j == 0:
                    triangle[i].append(1)
                elif j == i:
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i - 1][j] +
                    triangle[i - 1][j -1])
    return triangle
