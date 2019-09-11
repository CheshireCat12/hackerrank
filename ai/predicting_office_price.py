#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:42:25 2019

@author: cheshirecat12

Hackerrank exercise :
https://www.hackerrank.com/challenges/predicting-office-space-price/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics

def main():
    nb_features, len_dataset = [int(val) for val in input().split()]
    dataset = np.array([input().split() for _ in range(len_dataset)], float)
    len_validation_set = int(input())
    X_val = np.array([input().split() for _ in range(len_validation_set)], float)

    X, y = dataset[:,:-1], dataset[:,-1]

    l_model = LinearRegression()
    best_poly = (float("-INF"), 0)
    for i in range(1, 5):
        XtoP = PolynomialFeatures(i, include_bias=False)
        scores = cross_val_score(l_model, XtoP.fit_transform(X), y, cv=5)
        best_poly = max(best_poly, (scores.mean(), i), key=lambda x: x[0])

    _, poly = best_poly
    XtoP = PolynomialFeatures(poly, include_bias=False)
    final_model = LinearRegression()
    final_model.fit(XtoP.fit_transform(X), y)

    y_pred = final_model.predict(XtoP.fit_transform(X_val))
    print(*[round(val, 3) for val in y_pred], sep="\n")


if __name__ == "__main__":
    main()
