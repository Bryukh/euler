#-*- encoding: utf8 -*-

from optparse import OptionParser

def find_solution(task_number, var=0):
    task_name = "p" + str(task_number)
    #i can import solutions, but it import all tasks
    task = __import__("solutions." + task_name, fromlist=[task_name])
    solution_name = "solution" + (str(var) if var else '')
    if solution_name not in dir(task):
        print "Cann't find variant %d" % int(var)
        return None
    return getattr(task, solution_name)

def run_solution(solution):
    return solution()

def run_timing(solution):
    pass

def run_show(task_number, var=None):
    pass

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--timing", action="store_true",
                      help="Run with timing")
    parser.add_option("-s", "--show-variants", action="store_true",
                      help="Show variants of solutions")
    parser.add_option("-v", "--variant", type="int", dest="var",
                      default=0,
                      help="Select variant of solution")
    options, task_number = parser.parse_args()
    #print task_number
    #print options
    if not task_number:
        print "Please enter task number"
        exit()
    running_functions = [run_solution]
    if options.timing:
        running_functions.append(run_timing)

    for func in running_functions:
        solution = find_solution(task_number[0], options.var)
        if solution:
            print func(solution)