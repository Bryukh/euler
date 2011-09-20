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

from eulerfunc import eratosthenes

CONST=1000000

def solution(max_value=CONST):
    """
    Bryukh's solution
    """
    prime_lst = eratosthenes(max_value)
    res = 0
    len_res = 0
    for start in xrange(10):
        temp = 0
        for i in prime_lst[start:]:
            temp += i
            if temp > max_value:
                break
            if temp in prime_lst:
                if i - start > len_res:
                    len_res = i - start
                    res = temp
    return res


if __name__ == '__main__':
    pass
