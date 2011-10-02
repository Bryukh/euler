#-*- encoding: utf8 -*-
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.
If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from eulerfunc import is_curious_fraction
from fractions import Fraction

def solution():
    """Bryukh's solution"""
    res = 1
    for x in xrange(10, 100):
        for y in xrange(x+1, 100):
            if is_curious_fraction(x, y):
                res *= Fraction(x, y)
    return res



  