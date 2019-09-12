#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:51:05 2019

@author: cheshirecat12

hackerrank exercise:
https://www.hackerrank.com/challenges/predicting-house-prices/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
from sklearn.linear_model import LinearRegression


def main():
    F, H = [int(val) for val in input().split()]
    dataset = np.array([input().split() for _ in range(H)], float)
    T = int(input())
    X_val = np.array([input().split() for _ in range(T)], float)

    X_train, y_train = dataset[:, :-1], dataset[:, -1]

    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    y_pred = linear_model.predict(X_val)

    print(*[round(val, 3) for val in y_pred], sep="\n")


if __name__ == "__main__":
    main()
