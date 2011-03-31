from timeit import Timer
from p030 import self_sum, self_sum2

t1 = Timer("sum(self_sum(5))", "from __main__ import self_sum")
t2 = Timer("sum(self_sum2(5))", "from __main__ import self_sum2")
print "First with pow10 solution"
print t1.timeit(10)
print "First with int to str to int solution"
print t2.timeit(10)