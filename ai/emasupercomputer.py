#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:58:28 2019

@author: cheshirecat12

hackerrank exercise: Ema's Supercomputer

https://www.hackerrank.com/challenges/two-pluses/problem
"""


import math
import os
import random
import re
import sys

# Directions = [NORTH, EAST, SOUTH, WEST]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
GOOD_CELL = "G"


def _cells_per_plus(val):
    return (val-1)*4+1


def _is_in_grid_range(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def _is_valid_plus(cell, counter, unique_pluses, grid):
    save_directions = []

    for direction in DIRECTIONS:
        dir_x, dir_y = [d*counter+c for d, c in zip(direction, cell)]
        new_dir = (dir_x, dir_y)

        not_in_grid = not _is_in_grid_range(dir_x, dir_y, grid)
        is_overlapping = new_dir in unique_pluses

        if not_in_grid or grid[dir_y][dir_x] != GOOD_CELL or is_overlapping:
            return False
        save_directions.append((dir_x, dir_y))

    unique_pluses.update(save_directions)
    return True


def _plus(cell, unique_pluses, grid):
    counter = 1
    while _is_valid_plus(cell, counter, unique_pluses, grid):
        counter += 1
    return counter


# Complete the twoPluses function below.
def twoPluses(grid):
    unique_pluses = set()

    pluses_counter = [_cells_per_plus(_plus((x, y), unique_pluses, grid))
                      for y, row in enumerate(grid)
                      for x, cell in enumerate(row)
                      if cell == GOOD_CELL]
    print(pluses_counter)
    two_highest_val = sorted(pluses_counter, reverse=True)[:2]
    return two_highest_val[0] * two_highest_val[1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, m = [int(val) for val in input().split()]

    grid = [input() for _ in range(n)]

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
