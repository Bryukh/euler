#-*- encoding: utf8 -*-
"""
An irrational decimal fraction is created by concatenating
the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1  d10  d100  d1000  d10000  d100000  d1000000
"""
def irrational():
    count = 1
    while True:
        for c in str(count):
            yield int(c)
        count += 1

if __name__ == '__main__':
    searching = [10**j for j in xrange(7)]
    res = 1
    n = 1
    for i in irrational():
        if n in searching:
            res *= i
            print i
        if n == searching[-1]:
            break
        n += 1

    print res