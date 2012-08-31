"""
Just for tests
"""
import unittest

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

class Test(unittest.TestCase):
    def test_solutions(self):
        self.assertEqual(solution(1000), 1000)
        self.assertEqual(solution1(1000), 1000)

if __name__ == '__main__':
    unittest.main()