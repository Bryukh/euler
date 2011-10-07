# -*- coding: utf-8 -*-
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at 
least two positive integers?
"""
__author__ = 'bryukh'

CONST = 100

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()
    
    """
    p = [1, 1]
    for n in xrange(2, value+1):
        q = 1
        pn = 0
        while q <= n//2:
            ind1 = n-(3*(q**2)-q)/2
            ind2 = n-(3*(q**2)+q)/2
            t1 = p[ind1] if (ind1 >= 0 and ind1 < len(p)) else 0
            t2 = p[ind2] if (ind2 >= 0 and ind2 < len(p)) else 0
            pn += ((-1)**(q+1))*(t1 + t2)
            q += 1
        p.append(pn)
    return p[-1]-1

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)