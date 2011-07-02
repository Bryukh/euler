#!/usr/bin/env python
"""Find the sum of all the numbers that can be written as the sum
 of fifth powers of their digits."""
import math

def self_sum(digit):
    for x in xrange(2, 1000000):
        s = sum([math.pow(x // math.pow(10, p) % 10, digit) for p in xrange(digit + 1)])
        if s == x:
            yield s

def self_sum2(digit):
    for i in range(2, 1000000):
        total = 0
        for j in str(i):
            total += int(j) ** digit
        if total == i:
            yield total

if __name__ == '__main__':
#    for x in self_sum2(5):
#        print x
    print sum(self_sum2(5))
#    for x in self_sum(5):
#        print x
    print sum(self_sum(5))
