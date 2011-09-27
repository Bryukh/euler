# -*- coding: utf-8 -*-
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is
made up of each of the digits 0 to 9 in some order, but it also has
a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property
"""
__author__ = 'bryukh'

CONST = 9

from itertools import permutations

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()
    16695334890
    """
    res = 0
    check_list = [2, 3, 5, 7, 11, 13, 17]
    for var in permutations([str(x) for x in xrange(value+1)]):
        substrings = [int(''.join(var[i:i+3])) for i in xrange(1, 9)]
        if all([not substrings[i] % check_list[i] for i in xrange(7)]):
            print var
            res += int(''.join(var))
    return res


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
