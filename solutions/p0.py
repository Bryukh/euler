"""
Just for tests
"""
__author__ = 'bryukh'

CONST = 1000

def solution(value=CONST):
    """
    just empty
    
    >>> solution()
    1000
    """
    return value

def solution1(value=CONST):
    """
    alternative

    >>> solution()
    1000
    """
    value += 1
    return value-1

if __name__ == '__main__':
    import doctest
    doctest.testmod()