#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):

    if k == 0:
        return list(range(1, n+1))

    if n % (2*k) == 0:
        tmp = k
        permutation = []
        for i in range(1, n+1):
            permutation.append(i+tmp)

            if i % k == 0:
                tmp = -1 * tmp

        return permutation

    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n, k = [int(nk) for nk in input().split()]

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

