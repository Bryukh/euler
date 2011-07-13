#-*- encoding: utf8 -*-

def ispandigital(numb):
    return len(str(numb)) == 9 and set("123456789") == set(str(numb))

if __name__ == '__main__':
    for i in xrange(9876, 9183, -1):
        if ispandigital(int(str(i) + str(i*2))):
            print "Solution", i, i*2
            break
