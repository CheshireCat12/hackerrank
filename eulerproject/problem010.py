#!/bin/python3
from itertools import takewhile


def get_primes(num):
    """Compute the primes up to num."""
    primes = [2]
    candidate = 3
    while candidate <= num:
        if all(candidate % prime for prime in primes):
            primes.append(candidate)
        candidate += 2

    return primes


def main():
    t = int(input().strip())
    num_2_check = [int(input().strip()) for _ in range(t)]
    largest_num = max(num_2_check)
    primes = get_primes(largest_num)

    for num in num_2_check:
        sum_of_primes = sum(takewhile(lambda x: x <= num, primes))
        print(sum_of_primes)


if __name__ == "__main__":
    main()
