#-*- encoding: utf8 -*-
"""
It can be seen that the number, 125874, and its double, 251748, contain
exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

def solution():
    """
    Bryukh's solution
    """
    x = 1
    while True:
        lst_x = [x*i for i in xrange(2, 7)]
        lst_checks = [set(str(lx)) == set(str(x)) for lx in lst_x]
        if all(lst_checks):
            return x
        x += 1

if __name__ == '__main__':
    pass
