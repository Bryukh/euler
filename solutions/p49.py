# -*- coding: utf-8 -*-
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of
one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in
this sequence?
"""
__author__ = 'bryukh'

from eulerfunc import eratosthenes
from itertools import permutations

def solution():
    """
    Bryukh's solution
    >>> solution()
    [148748178147, 296962999629]
    """
    res = []
    pr_list = eratosthenes(10000)
    pr_list = pr_list[pr_list.index(1009):]
    while pr_list:
        pr = pr_list[0]
        pr_per = [int(''.join(var)) for var in permutations(str(pr))
                    if int(''.join(var)) in pr_list]
        pr_per = sorted(list(set(pr_per)))
        for x in pr_per:
            pr_list.remove(x)
        if len(set(pr_per)) < 3:
            continue
        for i in xrange(len(pr_per)-2):
            for j in xrange(i+1, len(pr_per)-1):
                third = pr_per[j] + (pr_per[j] - pr_per[i])
                if third in pr_per:
                    res.append(pr_per[i]*(10**8) + pr_per[j]*(10**4) + third)
    return res


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)