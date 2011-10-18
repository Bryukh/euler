# -*- coding: utf-8 -*-
"""
The 5-digit number, 16807=75, is also a fifth power. 
Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""
__author__ = 'bryukh'

CONST = 0

from math import log10

def solution():
    """
    Bryukh's solution
    >>> solution()
    
    """
    res = 0
    for base in xrange(1, 10):
        lim = int(1 / (1 - log10(base)))
        for n in xrange(1, lim+1):
            if len(str(base**n)) == n:
                res += 1
    return res


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)