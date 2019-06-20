#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product

_NEIGHBORS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (0, 0),
]

def _add(a, b):
    return [x+y for x, y in zip(a, b)]

def _is_valid_range(x, y, row, col):
    return 0 <= x < col and 0 <= y < row


def explose_bomb(coordinates, grid, row, col):
    for neighbor in _NEIGHBORS:
        x, y = _add(coordinates, neighbor)
        if not _is_valid_range(x, y, row, col):
            continue
        grid[y][x] = '.'


# Complete the bomberMan function below.
def bomberMan(row, col, n_steps, grid):
    n_steps -= 1

    if n_steps == 0:
        return grid

    new_grid = [["O"] * col for _ in range(row)]

    if n_steps % 2 != 0:
        return ["".join(val) for val in new_grid]

    if n_steps % 4 != 0:
        n_steps = 1
    else:
        n_steps = 2

    while n_steps > 0:
        for y, x in product(range(row), range(col)):
            if grid[y][x] == "O":
                explose_bomb((x, y), new_grid, row, col)

        grid = new_grid
        new_grid = [["O"] * col for _ in range(row)]
        n_steps -= 1

    return ["".join(val) for val in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    r, c, n = [int(val) for val in input().split()]

    grid = [input() for _ in range(r)]

    result = bomberMan(r, c, n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

