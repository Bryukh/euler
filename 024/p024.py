#!/usr/bin/env python
"""A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic
permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

def combination(variants):
    if variants:
        for i in variants:
            rvariants = variants[:]
            rvariants.remove(i)
            for u in combination(rvariants):
                yield [i] + u
    else:
        yield []

count = 1
for x in combination(range(10)):
    count += 1
    if count > 1000000:
        print ''.join([str(i) for i in x])
        exit()
