#-*- encoding: utf8 -*-
"""
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes
below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

from eulerfunc import eratosthenes

CONST=1000000

def solution(max_value=CONST):
    """
    Bryukh's solution
    """
    numb_list = range(2, max_value)
    circular = []
    numb_list = eratosthenes(max_value)
    for i in numb_list:
        if i in circular:
            continue
        rotations = set([int(str(i)[k:]+str(i)[:k])
                         for k in xrange(len(str(i)))])
        for numb in rotations:
            if not numb in numb_list:
                break
        else:
            circular += list(rotations)
    return len(circular)

