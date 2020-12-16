#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    idx = 1
    if len(matrix[0]) == 0:
        print("")
    else:
        for i in matrix:
            for x in i:
                if idx < len(i):
                    print("{:d}".format(x), end=" ")
                else:
                    print("{:d}".format(x))
                idx += 1
            idx = 1
