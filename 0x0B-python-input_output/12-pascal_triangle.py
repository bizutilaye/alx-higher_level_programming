#!/usr/bin/python3
"""
Module for pascal_triangle function
"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Args:
    - n: an integer representing the number of rows in the Pascal's triangle

    Returns:
    - A list of lists of integers representing the Pascal's triangle of n
    - An empty list if n <= 0

    Constraints:
    - Do not import any module
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

        row.append(1)
        triangle.append(row)

    return triangle
