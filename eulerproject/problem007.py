#!/bin/python3


def get_primes(size):
    """Compute the list of the first Nth prime."""
    primes = [2]
    candidate = 3

    while len(primes) < size:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 2

    return primes


def main():
    t = int(input().strip())
    prime_indices = [int(input().strip()) for _ in range(t)]
    largest_index = max(prime_indices)

    primes = get_primes(largest_index)

    for index in prime_indices:
        print(primes[index-1])


if __name__ == "__main__":
    main()
