# -*- coding: utf-8 -*-
"""
Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, 
as any calculator would confirm that 211 = 2048  37 = 2187.

However, confirming that 632382^518061  519432^525806 would be much more 
difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), 
a 22K text file containing one thousand lines with a base/exponent 
pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the 
example given above.
"""
__author__ = 'bryukh'

CONST = 0

from math import log

def solution():
    """
    Bryukh's solution
    >>> solution()
    
    """
    basef = open("eulerfiles/base_exp99.txt", "r")
    numbers = [map(int, line.strip().split(',')) for line in basef.readlines()]
    # numbers = [(int)]
    res = 0
    for i in xrange(1, len(numbers)):
        if ((numbers[res][1]*log(numbers[res][0])) <
                 (numbers[i][1]*log(numbers[i][0]))):
            print numbers[i]
            res = i
    return res+1


if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)