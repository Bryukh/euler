#!/usr/bin/env python
"""If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000."""

CONST = 1000

def solution(edge=CONST):
    "Bryukh's solution"
    sum3 = sum((x * 3 for x in xrange((edge - 1) // 3 + 1)))
    sum5 = sum((x * 5 for x in xrange((edge - 1) // 5 + 1)))
    sum15 = sum((x * 15 for x in xrange((edge - 1) // 15 + 1)))
    return (sum3 + sum5 - sum15)

def solution2(edge=CONST):
    "from https://github.com/nixeagle/euler"
    (y, rang) = (0, range(1, edge))
    for x in rang:
        if x % 3 == 0:
            y += x
        elif x % 5 == 0:
            y += x
    return y

if __name__ == "__main__":
    print solution()
    print solution()
