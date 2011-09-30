# -*- coding: utf-8 -*- """ It is possible to show that the square root of two
"""
can be expressed as an  infinite continued fraction.

 sqrt(2)=1+1/(2+1/(2+1/(2+...)))=1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4 
1 + 1/(2 + 1/(2 + 1/2)) = 17/12= 1.41666... 
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the
numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator
with more digits than denominator? """ 

__author__ = 'bryukh'

CONST = 1000

from fractions import Fraction

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()
    
    """
    count = 0
    for x in xrange(value):
        denominator = 2
        for _ in xrange(x+1):
            temp = Fraction(1, denominator)
            denominator = temp + 2
        expansion = 1 + temp
        if len(str(expansion.numerator)) > len(str(expansion.denominator)):
            count += 1
    return count
        
if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)