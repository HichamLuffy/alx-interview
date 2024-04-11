#!/usr/bin/python3
"""
pascal_triangle
"""


def pascal_triangle(n):
    """ Returns pascal triangle """
    Tlist = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(Tlist[i-1][j] + Tlist[i-1][j-1])
        Tlist.append(temp_list)
    return Tlist
