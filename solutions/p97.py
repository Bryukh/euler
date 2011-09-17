#-*- encoding: utf8 -*-
"""
The first known prime found to exceed one million digits was discovered in 1999,
and is a Mersenne prime of the form 2^6972593 - 1; it contains
exactly 2,098,960 digits. Subsequently other Mersenne primes, of
the form 2^p - 1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which
contains 2,357,207 digits: 28433*2^7830457+1.

Find the last ten digits of this prime number.
"""

def solution():
    """
    Bryukh's solution
    """
    res = 1
    for i in xrange(7830457):
        res = int(str(res*2)[-10:])
    res = int(str(res*28433+1)[-10:])
    return res

def solution1():
    """
    Fast solution using pow(x, y, z)
    Very useful option for pow().
    """
    return 28433*pow(2, 7830457, 10**10) % 10**10 + 1

if __name__ == '__main__':
    pass
