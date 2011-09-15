#-*- encoding: utf8 -*-
"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations
from eulerfunc import isprime, ispandigital

def solution():
    """
    Bryukh's solution
    """
    res = []
    for i in xrange(2, 10):
        perm_list = permutations(range(1, i+1))
        for var in perm_list:
            pandigit = int(''.join([str(x) for x in var]))
            if isprime(pandigit):
                res.append(pandigit)
                print pandigit
    return max(res)
