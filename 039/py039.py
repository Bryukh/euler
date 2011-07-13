#-*- encoding: utf8 -*-
"""
If p is the perimeter of a right angle triangle with integral
length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p<=1000, is the number of solutions maximised?
"""
if __name__ == '__main__':
    res = []
    for p in xrange(3, 1001):
        temp = [p]
        for a in xrange(1, p*2//3):
            for b in xrange(a, p*2//3):
                if a**2 + b**2 == (p-a-b)**2:
                    temp.append((a, b, p-a-b))
                    #print p, a, b, p-a-b
        if len(temp) > len(res):
            res = temp
    print res