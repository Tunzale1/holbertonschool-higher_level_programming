#!/usr/bin/python3
'''pascal triangle'''


def pascal_triangle(n):
    my_list = []
    if n <= 0 or type(n) is not int:
        return ValueError("n must be a positive integer.")
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = my_list[i - 1][j - 1] + my_list[i - 1][j]
        my_list.append(row)

    return my_list
