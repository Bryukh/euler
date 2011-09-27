# -*- coding: utf-8 -*-
"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?


"""
__author__ = 'bryukh'


if __name__ == "__main__":
    from doctest import testmod
    import os
    import sys
    sys.path.append(os.curdir)
    sys.path.append(os.pardir)
    testmod(verbose=True)

from eulerfunc import primedivisors, eratosthenes

CONST = 4

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution(2)
    14
    >>> solution(3)
    644
    """
    x = 10
    while True:
        if all([len(primedivisors(x+i).keys())==value for i in xrange(value)]):
            break
        x += 1
    return x

def solution1(value=CONST):
    """
    Bryukh's solution
    Try without primedivisors
    >>> solution(2)
    14
    >>> solution(3)
    644
    """
    pr_list = eratosthenes(100000)
    x = 10
    while True:
        x_divisors = [0] * value
        for i in range(value):
            for pr in pr_list:
                if not (x+i) % pr:
                    x_divisors[i] += 1
                if pr > (x+i)/2:
                    break
        if all([xd==value for xd in x_divisors]):
            break
        x += 1
    return x
#    res = {}
#    prime_list = list(eratosthenes(x))
#    while prime_list:
#        pr = prime_list[0]
#        #print pr, x
#        if x % pr:
#            prime_list.remove(pr)
#        else:
#            res[pr] = res[pr]+1 if pr in res.keys() else 1
#            if x == pr:
#                break
#            x = x / pr
#    return res

def solution2(value=CONST):
    """
    Bryukh's solution
    four time calculation in one
    >>> solution(2)
    14
    >>> solution(3)
    644
    """
    def count_div(numb, lst):
        res = 0
        for pr in lst:
            if not numb % pr:
                res += 1
            if pr > numb/2:
                if not res:
                    res = 1
                break
        return res

    pr_list = eratosthenes(100000)
    x = 10
    x_divisors = [0] * value
    for i in range(value):
        x_divisors[i] = count_div(x+i, pr_list)
    while True:
        if all([xd==value for xd in x_divisors]):
            break
        x += 1
        x_divisors = x_divisors[1:] + [count_div(x+value-1, pr_list)]
    return x

if __name__ == "__main__":
    solution2()