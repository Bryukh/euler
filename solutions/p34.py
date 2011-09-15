"""
TODO: need description
"""
__author__ = 'duov'

from eulerfunc import factorial

CONST=2500000

def solution(maxvalue=CONST):
    """
    Bryukh's solution
    """
    s = 0
    for d in xrange(3, maxvalue):
        if sum([factorial(int(c)) for c in str(d)]) == d:
            s += d
    return s