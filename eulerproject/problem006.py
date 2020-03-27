#!/bin/python3


def square_of_sum(n):
    """Compute the square of the sum of the n first natural numbers."""
    return (n*(n+1)//2)**2


def sum_of_squares(n):
    """Compute the sum of squares of the n first natural numbers."""
    return n*(n+1)*(2*n+1)//6


def absolute_diff(n):
    """
    Compute the absolute difference between the square of sum
    and the sum of squares.
    """
    return square_of_sum(n) - sum_of_squares(n)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(absolute_diff(n))
