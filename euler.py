#!/usr/bin/env python
#-*- encoding: utf8 -*-

__author__ = "Valentin Bryukhanov"

"""
#TODO: need docstring
"""

import os
import re

from timeit import Timer
from optparse import OptionParser


class SolutionError(Exception):
    """
    Solution exception
    """
    def __init__(self, ertext, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
        self.text = ertext

    def __str__(self):
        return repr(self.text)


class Solution(object):
    """
    Create solution object
    """

    def __init__(self, task_number, variant):
        """
        Check existence of solution
        """
        self._task_number = task_number
        self._variant = variant
        task_name = "p{0}".format(str(self._task_number))
        try:
            self._task = __import__("solutions." + task_name,
                                    fromlist=[task_name])
        except ImportError:
            raise SolutionError("Can't find solution file " +
                                "for problem {0}".format(self._task_number))
            #i can import solutions, but it import all tasks
        self._solution_name = ("solution" +
                               (str(self._variant) if self._variant else ''))
        if self._solution_name not in dir(self._task):
            raise SolutionError("Cann't find variant {0}".format(self._variant))
        self._solution_func = getattr(self._task, self._solution_name)

    def run_solution(self):
        """
        Run solution and return answer
        """
        return self._solution_func()

    def run_timing(self, quantity=1):
        """
        Run timing for solution quantity times
        """
        timer = Timer(self._solution_name + "()",
                      "from solutions.p{0} import {1}".format(
                          self._task_number, self._solution_name))
        time = timer.timeit(quantity)
        return time

    def run_show_vars(self):
        """
        Show exist variants and docstring for it
        """
        #TODO: Fill it
        pass

    @staticmethod
    def run_show_all():
        """
        Show existing solutions
        """
        files = os.listdir("solutions")
        pattern = re.compile(r"p\d*\.py$")
        tasks = [int(f[1:-3]) for f in files if re.match(pattern, f)]
        return ','.join([str(t) for t in sorted(tasks)])

    def run_show_task(self):
        """
        Show task description
        """
        return self._task.__doc__


def main():
    """
    Main function
    """
    parser = OptionParser()
    parser.add_option("-t", "--timing", action="store_true",
                      dest="timing",
                      help="Run with timing test")
    parser.add_option("-n", action="store", type="int",
                      dest="quantity", default=1,
                      help="How many times run solution")
    parser.add_option("-s", "--show-variants", action="store_true",
                      help="Show variants of solutions")
    parser.add_option("-v", "--variant", type="int", dest="var",
                      default=0,
                      help="Select variant of solution")
    parser.add_option("-a", "--show-solutions", dest="show_all",
                      action="store_true",
                      help="Show existing solutions")
    parser.add_option("-d", "--show-description", dest="description",
                      action="store_true",
                      help="Show task description")
    options, task_number = parser.parse_args()

    if options.show_all:
        print Solution.run_show_all()
        return None
    if not task_number:
        print "Please enter task number"
        exit()
    solution = Solution(task_number[0], options.var)
    if options.description:
        print solution.run_show_task()
    print "Variant ", "default" if not options.var else options.var
    print "Answer is", solution.run_solution()
    if options.timing:
        print "Timer for %d time is" % options.quantity, \
            solution.run_timing(quantity=options.quantity)

if __name__ == '__main__':
    main()
