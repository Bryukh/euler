#!/usr/bin/env python
"""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000."""
import math
from eulerfunc import last_pow_numb

def solution():
    """
    Bryukh's solution
    """
    l = math.pow(10, 10)
    s = sum([last_pow_numb(x, x, l) for x in xrange(1, 1001)])
    return s % l
    