#!/usr/bin/env python
"""The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000."""
import math

def last_pow_numb(base, pow, last):
    """function for last number in power"""
    return reduce(lambda x, y: (x * y) % last, [base] * (pow - 1), base)

if __name__ == "__main__":
    l = math.pow(10, 10)
    s = sum([last_pow_numb(x, x, l) for x in xrange(1, 1001)])
    print s % l
    