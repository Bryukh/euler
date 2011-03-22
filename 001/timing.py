from timeit import Timer
from problem_1 import sum3and5, sum3and5_v2

t1 = Timer("sum3and5(1000)", "from __main__ import sum3and5")
t2 = Timer("sum3and5_v2(1000)", "from __main__ import sum3and5_v2")
print t1.timeit(10000)
print t2.timeit(10000)