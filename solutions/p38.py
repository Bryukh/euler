#-*- encoding: utf8 -*-
"""
TODO: add description
"""

from eulerfunc import ispandigital

def solution():
    """
    Bryukh's solution
    """
    for i in xrange(9876, 9183, -1):
        if ispandigital(int(str(i) + str(i*2)), 9):
            return i*2
    return None
