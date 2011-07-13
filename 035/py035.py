#-*- encoding: utf8 -*-
"""
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes
below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

def eratosthenes(n):
    N=range(n+1)
    z=[0]*(n/2)
    for i in range(2, int(n**.5)+1):
        if N[i]:
            N[i*i::i] = z[:(n/i)-i+1]
    return filter(None, N[2:])

if __name__ == '__main__':
    numb_list = range(2, 1000000)
    circular = []
    numb_list = eratosthenes(1000000)
    for i in numb_list:
        if i in circular:
            continue
        rotations = set([int(str(i)[k:]+str(i)[:k]) for k in xrange(len(str(i)))])
        for numb in rotations:
            if not numb in numb_list:
                break
        else:
            circular += list(rotations)
    print circular
    print len(circular)

