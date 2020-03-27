#!/bin/python3
from functools import reduce


t = int(input().strip())
for a0 in range(t):
    n, k = [int(val) for val in input().strip().split(' ')]
    num = input().strip()
    prod_of_k = [reduce((lambda x, y: x * y), [int(val) for val in num[i:i+k]])
                 for i in range(len(num)-k+1)]
    print(max(prod_of_k))
