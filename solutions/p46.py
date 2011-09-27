# -*- coding: utf-8 -*-
"""
It was proposed by Christian Goldbach that every odd composite
number can be written as the sum of a prime and twice a square.

9 = 7 + 2*1^2
15 = 7 + 2*2^2
21 = 3 + 2*3^2
25 = 7 + 2*3^2
27 = 19 + 2*2^2
33 = 31 + 2*1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the
sum of a prime and twice a square?
"""
__author__ = 'bryukh'

CONST = 0

from eulerfunc import eratosthenes
from math import sqrt

def solution():
    """
    Bryukh's solution
    >>> solution()
    5777
    """
    n = 7
    prime_lst = eratosthenes(100000)
    while True:
        n += 2
        if n in prime_lst:
            continue
        for pr in prime_lst:
            if n < pr:
                return n
            diff = n - pr
            if not diff % 2 and sqrt(diff//2) == int(sqrt(diff//2)):
                break


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)  