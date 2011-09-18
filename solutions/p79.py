#-*- encoding: utf8 -*-
"""
A common security method used for online banking is to ask the user for
three random characters from a passcode. For example, if the passcode was
531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply
would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file
so as to determine the shortest possible secret passcode of unknown length.
"""

from itertools import permutations

def check_key(code, key):
    """
    Check key for passcode
    """
    if not all([ch in code for ch in key]):
        return False
    if all([code.index(key[j]) < code.index(key[j+1])
            for j in xrange(len(key)-1)]):
        return True
    return False

def solution():
    """
    Bryukh's solution
    """
    try:
        file = open("eulerfiles/keylog79.txt")
    except IOError:
        print "Can't open file"
        return None
    keys = [str(x)[:-2] for x in file.readlines()]
    ch_set = set(''.join(keys))
    for var in permutations(list(ch_set)):
        passcode = ''.join(var)
        for k in keys:
            if not check_key(passcode, k):
                break
        else:
            return passcode
    return None


if __name__ == '__main__':
    pass
