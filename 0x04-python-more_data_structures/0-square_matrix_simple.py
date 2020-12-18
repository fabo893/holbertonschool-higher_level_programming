#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return matrix
    else:
        new = []
        for y in range(0, len(matrix)):
            new1 = matrix[y][:]
            i = 0
            for x in matrix[y]:
                new1[i] = (x ** 2)
                i = i + 1
            new.append(new1)
    return new
