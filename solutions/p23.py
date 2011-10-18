#TODO: add description and change for performance

__author__ = 'bryukh'

from eulerfunc import isabundant


def solution():
    res_lst = []
    abundants = [x for x in xrange(12, 28123) if isabundant(x)]
    for current in xrange(1, 28123):
        for x in xrange(1, current):
            if x in abundants and (current - x) in abundants:
                break
        else:
            res_lst.append(current)
    return sum(res_lst)

if __name__ == '__main__':
    print solution()
