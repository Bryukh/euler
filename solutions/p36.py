#!/usr/bin/env python
"""The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2."""

from eulerfunc import isbinpalindrom



def solution():
    """
    Bryukh's solution
    """
    return sum([x for x in xrange(1, 1000000,2)
            if str(x) == str(x)[::-1] and isbinpalindrom(x)])