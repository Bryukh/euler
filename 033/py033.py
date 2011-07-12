#-*- encoding: utf8 -*-
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator
and denominator.
If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

from fractions import Fraction

def isCuriousFraction(numenator, denominator):
    """
    It is check fractions for task
    """
    snum = str(numenator)
    sden = str(denominator)
    for i in xrange(len(snum)):
        for j in xrange(len(sden)):
            if snum[i] != sden[j] or not int(snum[i]) or not int(sden[j]):
                continue
            newnum = int(snum[:i]+snum[i+1:])
            newden = int(sden[:j]+sden[j+1:])
            if not newden:
                continue
            if Fraction(numenator, denominator) == Fraction(newnum, newden):
                return True
    return False

if __name__ == '__main__':
    res = 1
    for x in xrange(10, 100):
        for y in xrange(x+1, 100):
            if isCuriousFraction(x, y):
                print "{0}/{1}".format(x,y)
                res *= Fraction(x, y)
    print "Answer - {0}".format(res)



  