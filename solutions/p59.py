# -*- coding: utf-8 -*-
"""
Each character on a computer is assigned a unique code and the preferred 
standard is ASCII (American Standard Code for Information Interchange). 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to 
ASCII, then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key 
on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, 
then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text 
message, and the key is made up of random bytes. The user would keep the 
encrypted message and the encryption key in different locations, and 
without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the 
modified method is to use a password as a key. If the password is 
shorter than the message, which is likely, the key is repeated cyclically 
throughout the message. The balance for this method is using a sufficiently 
long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower 
case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), 
a file containing the encrypted ASCII codes, and the knowledge that the plain 
text must contain common English words, decrypt the message and find the sum 
of the ASCII values in the original text.
"""
__author__ = 'bryukh'

CONST = 0

from itertools import product

def solution(value=CONST):
    """
    Bryukh's solution
    >>> solution()
    107359
    """
    crypt_file = open("eulerfiles/cipher59.txt", "r")
    cipher_list  = [int(s) for s in crypt_file.read(-1).strip().split(',')]
    for key in product(range(97, 123), repeat=3):
        temp = cipher_list[:]
        for i in xrange(0, len(temp), 3):
            size = 3 if (i+3)<=len(temp) else len(temp)-i
            temp[i:i+size] = [temp[i+j]^key[j] for j in xrange(size)]
        temp_str = ''.join(chr(x) for x in temp)
        if all([31<x<123 for x in temp]) and "the" in temp_str:
            return sum(temp)

if __name__ == "__main__":
    from doctest import testmod
    testmod(verbose=True)