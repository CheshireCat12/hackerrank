#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:36:29 2019

@author: cheshirecat12

Hackerrank exercise:
    https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
"""

import os


# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    """Count the number of transformation to change a string to a palindrome."""
    return sum(abs(ord(letter)-ord(s[-1-i]))
               for i, letter in enumerate(s[:len(s)//2]))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
