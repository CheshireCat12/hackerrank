#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:25:05 2019

@author: cheshirecat12

Hackerrank exercise: https://www.hackerrank.com/challenges/weighted-uniform-string/problem
"""


import os
from string import ascii_lowercase

map_letters = {letter: value+1
               for value, letter in enumerate(ascii_lowercase)}


# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    prev_letter = ""
    counter = 1
    uniform_string_weight = set()

    for i, letter in enumerate(s):
        if letter == prev_letter:
            counter += 1
        else:
            counter = 1
        prev_letter = letter

        uniform_string_weight.add(map_letters[letter]*counter)

    results = ["Yes" if querie in uniform_string_weight else "No"
               for querie in queries]
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = [int(input()) for _ in range(queries_count)]

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
