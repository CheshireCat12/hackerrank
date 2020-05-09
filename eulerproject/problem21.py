from math import ceil
from typing import List, Tuple, Set


_MAX = 10**5


def proper_divisors(num: int) -> List[Tuple[int, int]]:
    sqrt_num = ceil(num**(1/2))
    return [(i, num//i) for i in range(1, sqrt_num) if num % i == 0]


def sum_proper_divisors(num: int) -> int:
    # Remove first element because it contains the num
    divisors = proper_divisors(num)[1:]

    return sum(sum(val) for val in divisors) + 1


def get_amicables() -> Set[int]:
    """
    Compute all the amicable numbers below the _MAX value.
    """
    amicables = set()
    for candidate in range(1, _MAX):
        sum_div = sum_proper_divisors(candidate)
        amicable_candidate = sum_proper_divisors(sum_div)

        if candidate == amicable_candidate and sum_div != amicable_candidate:
            amicables.add(candidate)
            amicables.add(amicable_candidate)

    return amicables


def main():
    nb_tests = int(input().strip())

    amicables = get_amicables()

    for _ in range(nb_tests):
        num = int(input().strip())
        print(sum(val for val in amicables if val <= num))


if __name__ == '__main__':
    main()
