#!/bin/python3


def _mul(list_):
    res = 1
    for val in list_:
        res *= val
    return res


def main():
    length = 4
    grid_length = 20
    grid = [[int(grid_temp) for grid_temp in input().strip().split(' ')]
            for _ in range(grid_length)]
    grid_T = [list(row) for row in zip(*grid)]
    grid_reversed = grid[::-1]

    max_product = float('-inf')

    for i in range(grid_length):
        for j in range(grid_length-length+1):
            max_product = max(max_product, _mul(grid[i][j:j+length]))
            max_product = max(max_product, _mul(grid_T[i][j:j+length]))
            if i > grid_length - length:
                continue
            diag1 = [grid[i+k][j+k] for k in range(4)]
            diag2 = [grid_reversed[i+k][j+k] for k in range(4)]
            max_product = max(max_product, _mul(diag1))
            max_product = max(max_product, _mul(diag2))

    print(max_product)


if __name__ == "__main__":
    main()
