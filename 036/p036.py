#!/usr/bin/env python
"""The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2."""

from unittest import TestCase


def isbinpalindrom(numb):
        b = bin(int(numb))[2:]
        return b == b[::-1]

#Just learning unittest and TDD
class BinPalindromTest(TestCase):
    def test_binpalindrom(self):
        self.assertEqual(True, isbinpalindrom(585))

    def test_wrongParametrs(self):
        self.assertRaises(ValueError, isbinpalindrom, 'dsads')
        self.assertRaises(TypeError, isbinpalindrom, [])

if __name__ == '__main__':
    print sum([x for x in xrange(1, 1000000,2)
            if str(x) == str(x)[::-1] and isbinpalindrom(x)])