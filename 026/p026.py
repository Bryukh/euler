"""
A unit fraction contains 1 in the numerator. The decimal representation
of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.
"""
if __name__=='__main__':
    maxrep = 0
    best = 1
    for d in xrange(2, 1000):
        den = 1
        prev = []
        while 1:
            while den < d:
                den *= 10
            mod = den % d
            if not mod:
                break
            if mod in prev:
                rep = len(prev) - prev.index(mod)
                if rep>maxrep:
                    maxrep = rep
                    best = d
                break
            prev.append(mod)
            den = mod
    print maxrep, best