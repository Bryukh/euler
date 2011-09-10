#!/usr/bin/env python
"""Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"""

CONST=1001

def solution(size=CONST):
    """
    First dumb solution
    """
    res = 1
    x = 1
    for inc in xrange(2, size+1, 2):
        res += 4 * x + 10 * inc
        x += 4 * inc
    return res

def solution2(size=CONST):
    "Math solution"
    return sum([10*(i+1)+4*(i**2) for i in xrange(1, size, 2)]) + 1

if __name__ == "__main__":
    print solution()