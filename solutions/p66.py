# -*- coding: utf-8 -*-
"""
Consider quadratic Diophantine equations of the form:

x^2 – D*y^2 = 1

For example, when D=13, the minimal solution in x is 6492 – 131802 = 1.

It can be assumed that there are no solutions in positive integers
when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we
obtain the following:

3^2 – 2*2^2 = 1
2^2 – 3*1^2 = 1
9^2 – 5*4^2 = 1
5^2 – 6*2^2 = 1
8^2 – 7*3^2 = 1

Hence, by considering minimal solutions in x for D  7, the largest x is
obtained when D=5.

Find the value of D  1000 in minimal solutions of x for which the largest
value of x is obtained.
"""
__author__ = 'bryukh'

CONST = 1000

from math import sqrt
from fractions import Fraction

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()

    """
    numbx_max = {'numb':0, 'x': 0}
    for numb in xrange(7, value+1):
        a = a0 = int(sqrt(numb))
        if int(a0) ** 2 == numb: continue
        m = 0
        d = 1
        res = [a]
        aprox = Fraction(a)
        x = aprox.numerator
        y = aprox.denominator
        while (x ** 2 - numb * (y ** 2)) != 1:
            m = d * a - m
            d = (numb - m ** 2) // d
            a = (a0 + m) // d
            res.append(a)
            aprox = reduce(lambda i, j: j + Fraction(1, i), res[::-1])
            x = aprox.numerator
            y = aprox.denominator
        print "{0}^2 - {1}*{2}^2=1".format(x, numb, y)
        if x > numbx_max['x']:
            numbx_max['numb'] = numb
            numbx_max['x'] = x
    return numbx_max

if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)  