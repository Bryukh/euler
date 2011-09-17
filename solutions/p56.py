#-*- encoding: utf8 -*-
"""
A googol (10**100) is a massive number: one followed by one-hundred zeros;
100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100,
 what is the maximum digital sum?
"""

def solution():
    """
    Bryukh's solution
    """
    res = 0
    for a in xrange(1, 101):
        for b in xrange(1, 101):
            s = sum([int(x) for x in str(a**b)])
            res = s if s>res else res
    return res

if __name__ == '__main__':
    pass
