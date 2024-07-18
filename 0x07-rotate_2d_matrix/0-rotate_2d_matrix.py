#!/usr/bin/python3
""" Rotate two dimention Matrix """


def rotate_2d_matrix(matrix):
    """ Make n * n 2d matrix with 
    90 degree clockwise rotate
    """
    # Return the matrix
    replica = matrix[:]

    for i in range(len(matrix)):
        # column from matrix 
        column = [row[i] for row in replica]
        # reverse order for the matrix
        matrix[i] = column[::-1]
