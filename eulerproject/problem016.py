def main():
    n_tests = int(input().strip())
    for _ in range(n_tests):
        print(sum(int(val) for val in str(2**int(input().strip()))))


if __name__ == "__main__":
    main()
