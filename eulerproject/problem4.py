#!/bin/python3


def is_palindrome(num):
    """Check if the given number is a palindrome"""
    str_ = str(num)
    return str_ == str_[::-1]


def find_palindrom(num):
    """Find the largest palindrome of 3-digits product"""
    palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, i-1, -1):
            mul = i * j
            if mul > num:
                continue
            if mul <= palindrome:
                break
            if is_palindrome(mul) and mul < num:
                palindrome = mul

    return palindrome


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_palindrom(n))
