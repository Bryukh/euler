#-*- encoding: utf8 -*-
"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
from itertools import permutations

def ispandigital(numb, length):
    return (len(str(numb)) == length and
            set([str(x) for x in xrange(1, length+1)]) == set(str(numb)))

def isprime(numb):
    if numb <= 0:
        return False
    if numb != 2 and not numb % 2:
        return False
    for i in xrange(3, int(pow(numb, 0.5))+1, 2):
        if not numb % i:
            return False
    return True

if __name__ == '__main__':
    res = []
    for i in xrange(2, 10):
        perm_list = permutations(range(1, i+1))
        for var in perm_list:
            pandigit = int(''.join([str(x) for x in var]))
            if isprime(pandigit):
                res.append(pandigit)
                print pandigit
    print "Solution", max(res)
