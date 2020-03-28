#!/bin/python3


def sieve_of_eratosthenes(num):
    primes = [True] * (num+1)

    candidate = 2
    while candidate**2 <= num:
        if primes[candidate]:
            primes[candidate**2::candidate] = [False] *\
                    len(primes[candidate**2::candidate])

        candidate += 1
    primes[:2] = [False, False]

    return primes


def sum_of_primes(primes):
    tmp = []
    count = 0
    for i, is_prime in enumerate(primes):
        if is_prime:
            count += i
        tmp.append(count)

    return tmp


def main():
    t = int(input().strip())
    largest_num = 10**6

    primes = sieve_of_eratosthenes(largest_num)
    sum_ = sum_of_primes(primes)

    for _ in range(t):
        n = int(input().strip())
        print(sum_[n])


if __name__ == "__main__":
    main()
