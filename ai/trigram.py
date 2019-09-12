#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 10:57:30 2019

@author: cheshirecat12

hackerrank exercise:
https://www.hackerrank.com/challenges/the-trigram/problem
"""

import sys
from collections import Counter
from itertools import islice


def n_gram(n, sentence):
    return zip(*[list(islice(sentence, i, None)) for i in range(n)])


def main():
    text = sys.stdin.read().split(".")

    counters = [Counter(n_gram(3, sentence.split()))
                for sentence in text]

    tmp = Counter()
    for counter in counters:
        tmp += counter

    print(" ".join(tmp.most_common(1)[0][0]).lower())


if __name__ == '__main__':
    main()
