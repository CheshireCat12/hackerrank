#!/bin/python3


def _is_int(n):
    return n == int(n)


def pythagorean_triplet(n):
    """Find the biggest product of pythagorean triplet a*b*c=n"""
    triplet = -1

    for a in range(1, n//2):
        b = (n*(n-2*a))/(2*(n-a))
        c = n - a - b
        if _is_int(b):
            triplet = max(triplet, int(a * b * c))

    return triplet


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(pythagorean_triplet(n))


if __name__ == "__main__":
    main()
