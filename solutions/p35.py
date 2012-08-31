#-*- encoding: utf8 -*-
"""
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes
below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

CONST=1000000

def eratosthenes(numb):
    """
    Give list of primes numbers less than numb
    """
    nlst = range(numb + 1)
    z = [0] * (numb / 2)
    for i in range(2, int(numb ** .5) + 1):
        if nlst[i]:
            nlst[i * i::i] = z[:(numb / i) - i + 1]
    return filter(None, nlst[2:])

def solution(max_value=CONST):
    """
    Bryukh's solution
    """
    #numb_list = range(2, max_value)
    circular = set([])
    pr_list = eratosthenes(max_value)
    for i in pr_list:
        if i in circular:
            continue
        rotations = set([int(str(i)[k:]+str(i)[:k])
                         for k in xrange(len(str(i)))])
        if all([n in pr_list for n in rotations]):
            circular = circular.union(set([r for r in rotations if r < max_value]))
    #print circular
    return len(circular)

if __name__ == '__main__':
    print(solution(50))
    print(solution(97))
    print(solution(9350))
    print(solution(100))
    print(solution(1000))
    print(solution(10000))
    print(solution(100000))
    assert solution(100) == 13, "100 Not"
    assert solution(1000) == 25, "1000 Not"
    #assert solution(10000) == 33, "10000 Not"
    #assert solution(100000) == 43, "100000 Not"
