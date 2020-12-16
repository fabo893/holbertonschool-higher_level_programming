#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 1
    for i in matrix:
        for x in i:
            if idx < len(i):
                print(x, end=' ')
            else:
                print(x)
            idx += 1
        idx = 1
