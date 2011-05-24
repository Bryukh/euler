__author__ = 'bryukh'

def divisors(numb):
    numb = int(numb)
    return [x for x in xrange(2, numb//2+1) if not numb%x]

def isabundant(numb):
    "Checking whether a number is abundant"
    if numb <= 0:
        return False
    return numb < sum(divisors(numb))

if __name__=='__main__':
    res_lst = []
    abundants = [x for x in xrange(12, 28123) if isabundant(x)]
    for current in xrange(1, 28123):
        for x in xrange(1, current):
            if x in abundants and (current-x) in abundants:
                break
        else:
            res_lst.append(current)
    print sum(res_lst)