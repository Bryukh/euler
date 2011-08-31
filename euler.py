#-*- encoding: utf8 -*-

from timeit import Timer
from optparse import OptionParser

def find_solution(task_number, var=0):
    task_name = "p" + str(task_number)
    try:
        task = __import__("solutions." + task_name, fromlist=[task_name])
    except ImportError:
        print "Cann't find solution file for problem %d" % int(task_number)
        return None
    #i can import solutions, but it import all tasks
    solution_name = "solution" + (str(var) if var else '')
    if solution_name not in dir(task):
        print "Cann't find variant %d" % int(var)
        return None
    return task_name, solution_name

def run_solution(task_name, solution_name):
    task = __import__("solutions." + task_name, fromlist=[task_name])
    solution = getattr(task, solution_name)
    return  solution()

def run_timing(task_name, solution_name, quantity=1):
    #from problem001 import sum3and5, sum3and5_v2
    #print solution_name + "()"
    #print "from %s import %s" % (task_name, solution_name)
    timer = Timer(solution_name + "()",
               "from solutions.%s import %s" % (task_name, solution_name))
    time = timer.timeit(quantity)
    return time

def run_show(task_number, var=None):
    pass

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--timing", action="store", type="int",
                      dest="quantity",
                      help="Run with timing n times")
    parser.add_option("-s", "--show-variants", action="store_true",
                      help="Show variants of solutions")
    parser.add_option("-v", "--variant", type="int", dest="var",
                      default=0,
                      help="Select variant of solution")
    options, task_number = parser.parse_args()
    #print task_number
    print options
    if not task_number:
        print "Please enter task number"
        exit()
    names = find_solution(task_number[0], options.var)
    if names:
        print "Variant ", "default" if not options.var else options.var
        print "Solution is ", run_solution(*names)
        if options.quantity:
            print "Timer for %d time is" % options.quantity,\
                    run_timing(*names, quantity=options.quantity)


