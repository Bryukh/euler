# -*- coding: utf-8 -*-
"""
Euler published the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the
consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.


#Using computers, the incredible formula  n**2 − 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n**2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
def isprime(numb):
    if numb <= 0:
        return False
    for i in xrange(2, int(pow(numb, 0.5))+1):
        if not numb % i:
            return False
    return True

best = (1, 1, 1)
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        unt = 0
        i = 0
        while isprime(i**2 + a*i + b):
            i += 1
        if i-1 > best[0]:
            best = (i-1, a, b)
            print best

    
