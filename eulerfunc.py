#-*- encoding: utf8 -*-

def ispandigital(numb, length):
    return (len(str(numb)) == length and
            set([str(x) for x in xrange(1, length+1)]) == set(str(numb)))

def eratosthenes(n):
    N=range(n+1)
    z=[0]*(n/2)
    for i in range(2, int(n**.5)+1):
        if N[i]:
            N[i*i::i] = z[:(n/i)-i+1]
    return filter(None, N[2:])

def isprime(numb):
    if numb <= 0:
        return False
    if numb != 2 and not numb % 2:
        return False
    for i in xrange(3, int(pow(numb, 0.5))+1, 2):
        if not numb % i:
            return False
    return True

def fibonacci(max_value):
    a, b = 1, 2
    while b < max_value:
        yield b
        a, b = b, a+b

if __name__ == '__main__':
    pass
