#!/usr/bin/env python
"""Find the sum of all the numbers that can be written as the sum
 of fifth powers of their digits."""
import math

CONST=5

def solution(digit=CONST):
    "Solution with decimal divison"
    res = 0
    for x in xrange(2, 10**(digit+1)):
        s = sum([math.pow(x // math.pow(10, p) % 10, digit) for p in xrange(digit + 1)])
        if s == x:
            res += s
    return res

def solution1(digit=CONST):
    "Solution with string"
    res = 0
    for x in range(2, 10**(digit+1)):
        s = sum([int(j)**digit for j in str(x)])
        if s == x:
            res += s
    return res

if __name__ == '__main__':
    print solution()
