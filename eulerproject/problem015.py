from math import factorial as fact


def main():
    n_test = int(input().strip())
    for _ in range(n_test):
        m, n = [int(val) for val in input().strip().split(' ')]
        print(fact(m+n) // (fact(m) * fact(n)) % 1000000007)


if __name__ == "__main__":
    main()
