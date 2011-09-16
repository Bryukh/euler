#!/usr/bin/env python
#-*- encoding: utf8 -*-
"""

"""
#TODO: need docstring
import os
import re

from timeit import Timer
from optparse import OptionParser

def find_solution(tnumber, var=0):
    """
    Check existence for variant of solution and return module and function name
    """
    task_name = "p" + str(tnumber)
    try:
        task = __import__("solutions." + task_name, fromlist=[task_name])
    except ImportError:
        print "Can't find solution file for problem %d" % int(tnumber)
        return None
    #i can import solutions, but it import all tasks
    solution_name = "solution" + (str(var) if var else '')
    if solution_name not in dir(task):
        print "Cann't find variant %d" % int(var)
        return None
    return task_name, solution_name

def run_solution(task_name, solution_name):
    """
    Run solution and return answer
    """
    task = __import__("solutions." + task_name, fromlist=[task_name])
    solution = getattr(task, solution_name)
    return  solution()

def run_timing(task_name, solution_name, quantity=1):
    """
    Run timing for solution quantity times
    """
    timer = Timer(solution_name + "()",
               "from solutions.%s import %s" % (task_name, solution_name))
    time = timer.timeit(quantity)
    return time

def run_show_vars(tnumber, var=None):
    """
    Show exist variants and docstring for it
    """
    #TODO: Fill it
    pass

def run_show_all():
    """
    Show existing solutions
    """
    files = os.listdir("solutions")
    pattern = re.compile(r"p\d*\.py$")
    tasks = [int(f[1:-3]) for f in files if re.match(pattern, f)]
    return ','.join([str(t) for t in sorted(tasks)])

def run_show_task(task_name):
    """
    Show task description
    """
    task = __import__("solutions." + task_name, fromlist=[task_name])
    return task.__doc__

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
    #print task_number
    #print options
    if options.show_all:
        print run_show_all()
        return None
    if not task_number:
        print "Please enter task number"
        exit()
    names = find_solution(task_number[0], options.var)
    if options.description:
        print run_show_task(names[0])

    if names:
        print "Variant ", "default" if not options.var else options.var
        print "Answer is", run_solution(names[0], names[1])
        if options.timing:
            print "Timer for %d time is" % options.quantity, \
                run_timing(names[0], names[1], quantity=options.quantity)

if __name__ == '__main__':
    main()

