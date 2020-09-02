from typing import List

_LIMIT = 5000


def fibonacci() -> List[int]:
    fib_seq = [False] * (_LIMIT+1)
    fib1, fib2 = 0, 1
    count = 1
    length_fib = float('-inf')

    while length_fib < _LIMIT:
        fibn = fib1 + fib2
        count += 1
        length_fib = len(str(fibn))

        if not fib_seq[length_fib]:
            fib_seq[length_fib] = count

        fib1, fib2 = fib2, fibn

    return fib_seq


def main():
    fib_seq = fibonacci()

    nb_tests = int(input().strip())
    print(*[fib_seq[int(input().strip())] for _ in range(nb_tests)],
          sep='\n')


if __name__ == '__main__':
    main()
