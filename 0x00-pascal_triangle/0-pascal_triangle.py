#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Back a list of integers
    display the Pascal Triangle of n
    an empty list > 2
    """
   init = []
    if n <= 0:
        returninit
   init = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            curr =init[i - 1]
            temp.append(k[i - 1][j] +init[i - 1][j + 1])
        temp.append(1)
       init.append(temp)
    returninit
