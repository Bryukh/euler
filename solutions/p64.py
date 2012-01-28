# -*- coding: utf-8 -*-
"""
How many continued fractions for N <= 10000 have an odd period?
"""
__author__ = 'bryukh'

CONST = 10000

from math import sqrt

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()
    http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
    http://en.wikipedia.org/wiki/Periodic_continued_fraction
    """
    odd_count = 0
    for numb in xrange(1, value+1):
        period = 0
        a = a0 = int(sqrt(numb))
        m = 0
        d = 1
        if a0 ** 2 == numb: continue
        while a != 2 * a0:
            m = d * a - m
            d = (numb - m ** 2) // d
            a = (a0 + m) // d
            period += 1
        if period % 2:
            odd_count += 1
    return odd_count

if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)  