#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product

# Complete the funnyString function below.
def funnyString(s):
    s = [ord(val) for val in s]

    abs_val_original = [abs(a-b) for a, b in zip(s, s[1:])]
    abs_val_reverse = [abs(a-b) for a, b in zip(s[::-1], s[-2::-1])]

    all_equal = all(val1 == val2 for val1, val2
                    in zip(abs_val_original, abs_val_reverse))

    return "Funny" if all_equal else "Not Funny"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for _ in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

