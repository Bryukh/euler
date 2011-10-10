# -*- coding: utf-8 -*-
"""
The cube, 41063625 (345^3), can be permuted to produce
two other cubes: 56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly
three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations
of its digits are cube.
"""
__author__ = 'bryukh'

CONST = 5


def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()

    """
    i = 5
    cur_len = 3
    cube = 125
    while True:
        cube_lst = []
        while len(str(cube)) == cur_len:
            cube_lst.append(cube)
            i += 1
            cube = i ** 3
        mod_cube_lst = [sorted(str(c)) for c in cube_lst]
        for checked in cube_lst:
            if mod_cube_lst.count(sorted(str(checked))) == value:
                return checked
        cur_len += 1

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)
