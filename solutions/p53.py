#-*- encoding: utf8 -*-
"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(nr)!
,where r <= n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100,
are greater than one-million?
"""

from math import factorial

def solution():
    """
    Bryukh's solution
    """
    res = 0
    for n in xrange(1, 101):
        fn = factorial(n)
        for r in xrange(1, n+1):
            fr = factorial(r)
            fnr = factorial(n-r)
            Crn = fn / (fr * fnr)
            if Crn > 1000000:
                res += 1
    return res


if __name__ == '__main__':
    pass
