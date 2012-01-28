# -*- coding: utf-8 -*-
"""
By replacing the 1st digit of *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443,
56663, 56773, and 56993. Consequently 56003, being the first member of this
family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part
of an eight prime value family.
"""

__author__ = 'bryukh'

CONST = 0

from eulerfunc import eratosthenes
from itertools import combinations

def repeating_digit(numb, n):
    """
    Check numb for n or greater repeating digit
    """
    snumb = str(numb)
    for i in xrange(10):
        if snumb.count(str(i)) >= n:
            return True
    return False

def find_template(numb, n):
    """
    Find template for repeating number
    """
    snumb = str(numb)
    temp = []
    strnumb = "0123456789"
    for s in strnumb:
        if snumb.count(s) >= n:
            wide_temp = [k for k in xrange(len(snumb)) if snumb[k] == s]
            temp += combinations(wide_temp, n)
    return temp


def generate_numb(base, template):
    """
    generate numbers from template
    """
    res = []
    sbase = str(base)
    for i in "0123456789":
        res.append(int(''.join([i if k in template else sbase[k]
                        for k in range(len(sbase))])))
    return res

def solution(value=CONST):
    """
    Bryukh's solution
    We can check only 3 repeat numbers
    >>> solution()
    
    """
    prime_lst = [pr for pr in eratosthenes(999999) if repeating_digit(pr, 3)]
    for prime in prime_lst:
        templates = find_template(prime, 3)
        #print prime, template
        for temp in templates:
            gen_lst = generate_numb(prime, temp)
            count = sum([1 for gen in gen_lst if gen in prime_lst])
            if count >= 8:
                return prime

if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)  