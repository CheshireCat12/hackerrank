from collections import defaultdict


def collatz(n, memoize):
    if n <= 1:
        memoize[1] = 1
        return 1

    if memoize[n]:
        return memoize[n]

    if n % 2 == 0:
        memoize[n] = 1 + collatz(n//2, memoize)
        return memoize[n]

    memoize[n] = 1 + collatz(3*n+1, memoize)
    return memoize[n]


def collatz_seq(n, memoize):
    longest_seq = (float('-inf'), None)

    for i in range(1, n+1):
        collatz(i, memoize)

        longest_seq = max(longest_seq, (memoize[i], i))

    return longest_seq[-1]


def main():
    memoize = defaultdict(bool)
    nb_tests = int(input().strip())
    n_2_test = [int(input().strip()) for _ in range(nb_tests)]
    max_num = max(n_2_test)

    collatz_seq(max_num, memoize)

    for num in n_2_test:
        print(collatz_seq(num, memoize))


if __name__ == "__main__":
    main()
