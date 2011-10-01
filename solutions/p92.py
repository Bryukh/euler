# -*- coding: utf-8 -*-
"""
A number chain is created by continuously adding the 
square of the digits in a number to form a new number until it has 
been seen before.

For example,

44  32  13  10  1  1
85  89  145  42  20  4  16  37  58  89

Therefore any chain that arrives at 1 or 89 will become stuck in an 
endless loop. What is most amazing is that EVERY starting number will 
eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
__author__ = 'bryukh'

CONST = 10000000

def solution(value=CONST):
    """
    Bryukh's solution
    Dumb solution
    >>> solution()
    8581146
    """
    count = 0
    for x in xrange(1, value):
        numb = x
        while True:
            numb = sum([(int(s))**2 for s in str(numb)])
            if numb == 89:
                count += 1
                break
            elif numb == 1:
                break
    return count

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)