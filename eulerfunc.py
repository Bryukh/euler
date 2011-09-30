#-*- encoding: utf8 -*-

from fractions import Fraction
import math

def factorial(numb):
    """
    Simple factorial
    """
    return reduce(lambda x, y: x*y, range(1, numb+1)) if numb else 1

def isCuriousFraction(numenator, denominator):
    """
    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.
    """
    snum = str(numenator)
    sden = str(denominator)
    for i in xrange(len(snum)):
        for j in xrange(len(sden)):
            if snum[i] != sden[j] or not int(snum[i]) or not int(sden[j]):
                continue
            newnum = int(snum[:i]+snum[i+1:])
            newden = int(sden[:j]+sden[j+1:])
            if not newden:
                continue
            if Fraction(numenator, denominator) == Fraction(newnum, newden):
                return True
    return False


def ispandigital(numb, length):
    """
    TODO: add description
    """
    return (len(str(numb)) == length and
            set([str(x) for x in xrange(1, length+1)]) == set(str(numb)))

def eratosthenes(numb):
    """
    Give list of primes numbers less than numb
    """
    N = range(numb+1)
    z = [0]*(numb/2)
    for i in range(2, int(numb**.5)+1):
        if N[i]:
            N[i*i::i] = z[:(numb/i)-i+1]
    return filter(None, N[2:])

def isprime(numb):
    if numb <= 0:
        return False
    if numb != 2 and not numb % 2:
        return False
    for i in xrange(3, int(pow(numb, 0.5))+1, 2):
        if not numb % i:
            return False
    return True

def fibonacci(max_value):
    a, b = 1, 2
    while b < max_value:
        yield b
        a, b = b, a+b

def divisors(numb):
    numb = int(numb)
    return [x for x in xrange(2, numb//2+1) if not numb%x]

def isabundant(numb):
    """Checking whether a number is abundant"""
    if numb <= 0:
        return False
    return numb < sum(divisors(numb))

def isbinpalindrom(numb):
    """
    The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
    """
    b = bin(int(numb))[2:]
    return b == b[::-1]

def last_pow_numb(base, power, last):
    """function for last number in power"""
    return reduce(lambda x, y: (x * y) % last, [base] * (power - 1), base)

def irrational():
    """
    An irrational decimal fraction is created by concatenating
    the positive integers:
    0.123456789101112131415161718192021...
    """
    count = 1
    while True:
        for c in str(count):
            yield int(c)
        count += 1

def triangle(n):
    """
    Find n-th tiangle number
    """
    return (n * (n + 1)) / 2

def ispentagonal(x):
    """
    Tests for pentagonal numbers
    """
    n = (math.sqrt(24*x+1) + 1) / 6
    return int(n) == n

def ishexagonal(x):
    """
    Tests for hexagonal numbers
    """
    n = (math.sqrt(8*x+1) + 1) / 4
    return int(n) == n

def primedivisors(x):
    """
    return dictionary of prime divisors and it's power

    >>> primedivisors(17)
    {17: 1}
    >>> primedivisors(99)
    {11: 1, 3: 2}
    >>> primedivisors(100)
    {2: 2, 5: 2}
    """
    res = {}
    prime_list = list(eratosthenes(x))
    while prime_list:
        pr = prime_list[0]
        #print pr, x
        if x % pr:
            prime_list.remove(pr)
        else:
            res[pr] = res[pr]+1 if pr in res.keys() else 1
            if x == pr:
                break
            x = x / pr
    return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
