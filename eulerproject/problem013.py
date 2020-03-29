def sum_50_digits(n_50_digits):
    n_50_digits_T = list(zip(*n_50_digits))
    carry = 0
    total_sum = []
    for val in n_50_digits_T:
        sum_ = sum(val) + carry
        total_sum.append(str(sum_)[-1])
        carry = int(str(sum_)[:-1]) if sum_ > 9 else 0
    total_sum.append(str(carry))
    return "".join(total_sum[::-1])


def main():
    n_tests = int(input().strip())
    n_50_digits = [[int(digit) for digit in input().strip()][::-1]
                   for _ in range(n_tests)]
    print(sum_50_digits(n_50_digits)[:10])


if __name__ == "__main__":
    main()
