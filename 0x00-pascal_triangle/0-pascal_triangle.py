#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Back a list of integers
    display the Pascal Triangle of n
    an empty list >
    """
    start_list = []
    if n <= 0:
        return start_list
    start_list = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(start_list[i - 1]) - 1):
            curr = start_list[i - 1]
            temp.append(start_list[i - 1][j] + start_list[i - 1][j + 1])
        temp.append(1)
        start_list.append(temp)
    return start_list
