# -*- coding: utf-8 -*-
"""
A positive fraction whose numerator is less than 
its denominator is called a proper fraction.
For any denominator, d, there will be d1 proper 
fractions; for example, with d = 12:
1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.
Furthermore we shall define the resilience of a denominator, R(d), to be the 
ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""
__author__ = 'bryukh'

CONST = 15499, 94744

from fractions import Fraction
from eulerfunc import euler_phi

def solution(value=CONST):
    """
    Bryukh's solution
    Very very very long solution
    >>> solution()
    
    """
    Rd_edge = Fraction(value[0], value[1])
    den = 1
    Rd = 1
    while Rd >= Rd_edge:
        den += 1
        res = euler_phi(den)
        Rd = Fraction(res, den-1)
        print den, Rd
    return den

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)