#!/usr/bin/env python
"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""
#Dumb solution
def spiral_array(side):
    ar = [[0] * side for t in range(side)]
    if not side % 2:
        return 0
    center = side // 2
    i = 1
    step = 1
    ar[center][center] = i
    x = center
    y = center
    i += 1
    try:
        while 1:
            #move right
            for j in range(1, step + 1):
                y += 1
                ar[x][y] = i
                i += 1
            #move down
            for j in range(1, step + 1):
                x += 1
                ar[x][y] = i
                i += 1
            step += 1
            #move left
            for j in range(1, step + 1):
                y -= 1
                ar[x][y] = i
                i += 1
            #move up
            for j in range(1, step + 1):
                x -= 1
                ar[x][y] = i
                i += 1
            step += 1
    except IndexError:
        return ar

def diag_sum(sq_list):
    if type(sq_list) != type([]) and type(sq_list[0]) != type([]):
        return 0
    first_diag = [sq_list[c][c] for c in xrange(len(sq_list))]
    second_diag = [sq_list[c][-c - 1] for c in xrange(len(sq_list))]
    return sum(first_diag) + sum(second_diag) - sq_list[len(sq_list) // 2][len(sq_list) // 2]

if __name__ == "__main__":
    sp = spiral_array(1001)
    if sp:
        for p in sp:
            print p
        print diag_sum(sp)
