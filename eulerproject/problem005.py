#!/bin/python3


def smallest_multiple(num):
    """
    Find the smallest positive number that is divisible
    by the numbers from 1 to num.
    """
    numbers = list(range(1, num))[::-1]
    candidate = num

    while True:
        if all(candidate % nb == 0 for nb in numbers):
            return candidate

        candidate += num


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_multiple(n))
