# -*- coding: utf-8 -*-
"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the 
bottom right, by only moving to the right and down, is indicated in bold 
red and is equal to 2427.


131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum, in matrix.txt (right click and 
'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, 
from the top left to the bottom right by only moving right and down.
"""
__author__ = 'bryukh'

CONST = 0

def solution():
    """
    Bryukh's solution
    >>> solution()
    427337
    """
    matrix_file = open("eulerfiles/matrix81.txt", "r")
    matrix = []
    for line in matrix_file.readlines():
        matrix.append([int(s) for s in line.strip().split(",")])
    len_m = len(matrix)
    dist_matrix = [[-1]*len_m for _ in xrange(len_m)]
    unchecked = [(x, y) for x in xrange(len_m) for y in xrange(len_m)]
    xc, yc = 0, 0
    dist_matrix[xc][yc] = matrix[xc][yc]
    while True:
        if xc+1 < len_m:
            if (dist_matrix[xc+1][yc] == -1 or 
                (matrix[xc+1][yc]+dist_matrix[xc][yc]) < dist_matrix[xc+1][yc]):
                dist_matrix[xc+1][yc] = matrix[xc+1][yc]+dist_matrix[xc][yc]
        if yc+1 < len_m:
            if (dist_matrix[xc][yc+1] == -1 or 
                (matrix[xc][yc+1]+dist_matrix[xc][yc]) < dist_matrix[xc][yc+1]):
                dist_matrix[xc][yc+1] = matrix[xc][yc+1]+dist_matrix[xc][yc]
        unchecked.remove((xc,yc))
        if not unchecked:
            break
        dist_dict = dict([(dist_matrix[x][y], (x, y))
                            for (x, y) in unchecked if dist_matrix[x][y] != -1])
        xc, yc = dist_dict[min(dist_dict.keys())]
    return dist_matrix[-1][-1]


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)