#!/usr/bin/env python
"""How many Sundays fell on the first of the month during the twentieth century
 (1 Jan 1901 to 31 Dec 2000)?"""

from datetime import date

CONST = 1901, 2001

def solution(begin=CONST[0], end=CONST[1]):
    "Bryukh's solution"
    count = 0
    for y in xrange(begin, end):
        for m in xrange(1, 13):
            if date(y, m, 1).weekday() == 6:
                count += 1
    return count


if __name__ == '__main__':
    #Answer: 171
    print solution()