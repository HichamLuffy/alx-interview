#!/usr/bin/python3
"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D matrix"""
    n = len(matrix)
    if matrix:
        try:
            for i in range(len(matrix)):
                for j in range(i, len(matrix)):
                    matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
            for i in range(n):
                matrix[i] = matrix[i][::-1]
        except ValueError:
            print("Error - matrix is None")

# my Debugging steps hhhhhhhhhh
# def rotate_2d_matrix(mat):
#     """Rotate 2D matrix"""
#     n = len(mat)
#     # make transpose of the matrix
#     for i in range(len(mat)):
#         print("i will use ", mat[i], "in :")
#         print("this matrix: ")
#         for row in mat:
#             print(row)
#         for j in range(i, len(mat)):
#             print("am changing ", mat[i][j], "to ", mat[j][i])
#             print("and am changing ", mat[j][i], "to ", mat[i][j])
#             mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
#         print("\n")
#         print("\n")
#         for i in range(n):
#             print("am reversing",mat[i])
#             mat[i] = mat[i][::-1]
#             print("am now: ", mat[i])
