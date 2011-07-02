#!/usr/bin/env python
"""How many Sundays fell on the first of the month during the twentieth century
 (1 Jan 1901 to 31 Dec 2000)?"""

from datetime import date

if __name__ == '__main__':
    #Answer: 171
    count = 0
    for y in xrange(1901, 2001):
        for m in xrange(1, 13):
            if date(y, m, 1).weekday() == 6:
                count += 1
    print count
