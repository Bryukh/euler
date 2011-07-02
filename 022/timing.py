from sys import exit
import timeit

try:
    fname = open('names.txt', 'r')
except IOError:
    print 'Couldn\'t open \"names.txt\"'
    exit()
name_list = fname.read().strip('\"').split('\",\"')
t1 = timeit.Timer('total_scores(name_list)',
                  "from problem022 import total_scores\n" + 
                  "from __main__ import name_list")
print t1.repeat(3, 100)
