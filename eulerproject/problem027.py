# import numpy as np
from itertools import product


def sieve_primes():
    n = 10**7
    primes = [True] * (n+1)
    idx = 2

    while idx*idx <= n:
        if primes[idx]:

            for i in range(idx*idx, n+1, idx):
                primes[i] = False
        idx += 1 if idx == 2 else 2

    return primes


def main():
    primes = sieve_primes()

    n_limit = int(input())
    count_sequence = (float('-inf'), 0, 0)
    a_seq = [val for val in range(-n_limit, n_limit) if val % 2 != 0]
    b_seq = [prime for prime in range(n_limit) if primes[prime]]

    for a, b in product(a_seq, b_seq):
        n = 0

        while n**2 + a*n + b > 0 and primes[n**2 + a*n + b]:

            if n > count_sequence[0]:
                count_sequence = (n, a, b)

            n += 1

    print(*count_sequence[1:])


if __name__ == '__main__':
    main()
