#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 18:33:40 2019

@author: cheshirecat12

hackerrank exercise:
    https://www.hackerrank.com/challenges/a-text-processing-warmup/problem
"""
import re


def main():
    n_texts = int(input())

    the_pattern = r"the |The "
    a_pattern = r"[^a-zA-Z](a |A )"
    an_pattern = r"[^a-zA-Z](an |An )"
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    months = "|".join(months)
    month_pattern = f"\d{{1,2}}(st|nd|rd|th)?( of)? ({months}),? (\d{{4}}|\d{{2}})"\
                    f"|{months} \d{{2}}, \d{{4}}"\
                    f"|\d{{2}}/\d{{2}}/(\d{{4}}|\d{{2}})"

    patterns = [a_pattern, an_pattern, the_pattern, month_pattern]

    for i in range(n_texts*2-1):
        if i % 2 != 0:
            input()
            continue

        text = input()

        [print(len(re.findall(pattern, text))) for pattern in patterns]


if __name__ == "__main__":
    main()
