#!/usr/bin/python3
"""
Module for generating Pascal's Triangle
"""


#!/usr/bin/python3
def pascal_triangle(n):
    """
    Creates a list of lists representing Pascal's Triangle of size n.

    Args:
        n (int): The number of rows in Pascal's Triangle

    Returns:
        list: A list of lists containing integers representing Pascal's Triangle
              Returns empty list if n <= 0

    Example:
        >>> pascal_triangle(3)
        [[1], [1, 1], [1, 2, 1]]
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        >>> pascal_triangle(0)
        []
    """
    if type(n) is int:
        if n <= 0:
            return []
        triangle = [[1]]
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle
    else:
        return []
