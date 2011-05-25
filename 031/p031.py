# -*- coding: utf-8 -*-
"""
In England the currency is made up of pound, £, and pence, p, and there
are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""
from itertools import product

SUMM = 200
COINS = [1, 2, 5, 10, 20, 50, 100, 200][::-1]

#It's stupid, slow solution. Very slow
if __name__=="__main__":
    count = 0
    max_quant = [SUMM/i for i in COINS]
    for var in product(*[range(m+1) for m in max_quant]):
        if sum([COINS[i]*var[i] for i in xrange(len(COINS))]) == SUMM:
            print var
            count += 1
    print count