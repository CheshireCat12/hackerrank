#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the alternate function below.
def alternate(s):
    chars = set(s)

    if len(chars) < 2:
        return 0

    res = 0

    # Can do better with walruse operator ?
    for chars_to_remove in combinations(chars, len(chars)-2):
        tmp = re.sub('|'.join(chars_to_remove), '', s)

        # Check if there are 2 consecutive same letters
        if not re.search(r'(\w)\1', tmp):
            res = max(res, len(tmp))

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _ = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()

