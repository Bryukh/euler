#-*- encoding: utf8 -*-
"""
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def eratosthenes(n):
    N=range(n+1)
    z=[0]*(n/2)
    for i in range(2, int(n**.5)+1):
        if N[i]:
            N[i*i::i] = z[:(n/i)-i+1]
    return filter(None, N[2:])

if __name__ == '__main__':
    prime_list = eratosthenes(1000000)
    res = []
    for pr in prime_list:
        if (all([(int(str(pr)[i:]) in prime_list and
                    int(str(pr)[:i+1]) in prime_list)
                for i in xrange(len(str(pr)))])):
            res.append(pr)
    print sum(res[-11:])