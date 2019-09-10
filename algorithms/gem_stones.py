#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:37:57 2019

@author: cheshirecat12

hackerrank exercise:
    https://www.hackerrank.com/challenges/gem-stones/problem
"""

import os


# Complete the gemstones function below.
def gemstones(arr):
    result = set.intersection(*[set(val) for val in arr])

    return len(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = [input() for _ in range(n)]

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
