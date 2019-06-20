#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    position = list(range(1, n+1))
    for permutation in permutations(position):
        if all(abs(pos-perm) == k
               for pos, perm
               in zip(position, permutation)):
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

