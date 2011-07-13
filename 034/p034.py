__author__ = 'duov'


def factorial(numb):
    return reduce(lambda x,y: x*y, range(1,numb+1)) if numb else 1

s = 0
for d in xrange(3, 2500000):
    if sum([factorial(int(c)) for c in str(d)]) == d:
        print d
        s += d
print s