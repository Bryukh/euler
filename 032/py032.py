#-*- encoding: utf8 -*-
"""
We shall say that an n-digit number is pandigital
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
"""
from itertools import permutations

def lst_to_int(lst):
    return int(''.join([str(x) for x in lst]))

__author__ = 'bruykh'
res = []
for var in permutations(range(1, 10)):
    for i in xrange(1, 5):
        a = lst_to_int(var[:i])
        b = lst_to_int(var[i:5])
        c = lst_to_int(var[5:])
        if a*b == c:
            res.append(c)
            print a,b,c
print sum(set(res))