#-*- encoding: utf8 -*-
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most
consecutive primes?
"""

from eulerfunc import eratosthenes, isprime

def solution():
    """
    Bryukh's solution
    """
    prime_lst = eratosthenes(1000000)
    res = 0
    for i in xrange(len(prime_lst)):
        #print i
        temp = sum(prime_lst[:i])
        if  isprime(temp):
            if temp > 1000000:
                max_shift = 1000000 - res
                j = 0
                while prime_lst[j] < max_shift:
                    shift_temp = sum(prime_lst[j:i])
                    if isprime(shift_temp) and res < shift_temp < 1000000:
                        res = sum(prime_lst[j:i])
                    j += 1
                return res
            res = temp
    return None


if __name__ == '__main__':
    pass
