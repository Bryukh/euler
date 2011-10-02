# -*- coding: utf-8 -*-
"""
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any 
order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest 
sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any 
two primes concatenate to produce another prime.
"""
__author__ = 'bryukh'

CONST = 0

from eulerfunc import eratosthenes, isprime
from itertools import combinations

def conc(n1, n2):
    """
    concatenate n1 and n2
    """
    return int(str(n1)+str(n2))

def not_conc_prime(n1, n2):
    return not isprime(conc(n1, n2)) or not isprime(conc(n2, n1))

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()
    26033
    """
    prlist = eratosthenes(10000)
    for p1 in prlist[:-4]:
        for p2 in prlist[prlist.index(p1)+1:-3]:
            if not_conc_prime(p1, p2):
                continue
            for p3 in prlist[prlist.index(p2)+1:-2]:
                if not_conc_prime(p1, p3) or not_conc_prime(p2, p3):
                    continue
                for p4 in prlist[prlist.index(p3)+1:-1]:
                    if (not_conc_prime(p1, p4) or not_conc_prime(p2, p4) or
                        not_conc_prime(p3, p4)):
                        continue
                    for p5 in prlist[prlist.index(p4)+1:]:
                        if (not_conc_prime(p1, p5) or not_conc_prime(p2, p5) or
                        not_conc_prime(p3, p5) or not_conc_prime(p4, p5)):
                            continue
                        return sum((p1, p2, p3, p4, p5))


    # for var in combinations(pr_list, 5):
    #     print var
    #     for pair in combinations(var, 2):
    #         if (not isprime(int(str(pair[0])+str(pair[1]))) or 
    #             not isprime(int(str(pair[1])+str(pair[0])))):
    #             break
    #     else:
    #         print var
    #         return sum(var)

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)