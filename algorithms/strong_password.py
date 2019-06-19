#!/bin/python3

import math
import os
import random
import re
import sys

_MIN_LENGTH = 6
_PATTERNS = [r'[0-9]',
             r'[a-z]',
             r'[A-Z]',
             r'[!@#$%^&*()-+-]']

# Complete the minimumNumber function below.
def minimumNumber(len_pass, password):
    """Return the minimum number of characters to make the password strong"""
    missing_char = sum(not(bool(re.search(pattern, password)))
                       for pattern in _PATTERNS)

    return max(max(0, _MIN_LENGTH - len_pass), missing_char)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

