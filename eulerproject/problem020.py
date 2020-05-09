def create_factorial(num):
    factorials = [1] * (num+1)
    for i in range(1, num+1):
        factorials[i] = factorials[i-1]*i

    return factorials


def main():
    nb_tests = int(input().strip())
    num_2_test = [int(input()) for _ in range(nb_tests)]
    num_max = max(num_2_test)
    factorials = create_factorial(num_max)

    for num in num_2_test:
        print(sum(int(val) for val in str(factorials[num])))


if __name__ == '__main__':
    main()
