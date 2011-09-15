#-*- encoding: utf8 -*-
"""
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to
its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the
word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""

def solution():
    """
    bryukh's solution
    """
    triagle_numbs = [(n*(n+1))/2 for n in xrange(1, 100)]
    words_file = open("eulerfiles/words42.txt", "r")
    words_str = words_file.read()
    words = words_str.replace('\"', '').split(',')
    count = 0
    for w in words:
        if sum([ord(c)-64 for c in w]) in triagle_numbs:
            #print w
            count +=1
    words_file.close()
    return count