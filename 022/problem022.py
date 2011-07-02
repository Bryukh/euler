#!/usr/bin/env python
"""Using names.txt, a 46K text file containing over five-thousand first names,
 begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?"""

def total_scores(name_list):
    """871198282"""
    name_list.sort()
    score_list = [sum((ord(ch) - 64 for ch in name)) for name in name_list]
    return sum((i * score_list[i - 1] for i in xrange(1, len(score_list) + 1)))

if __name__ == "__main__":
    try:
        fname = open("names.txt", "r")
    except IOError:
        print "Couldn't open \'names.txt\'"
        exit()
    name_list = fname.read().strip('\"').split('\",\"')
    print total_scores(name_list)
