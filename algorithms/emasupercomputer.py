#!/bin/python3
import os
from itertools import combinations

# Directions = [NORTH, EAST, SOUTH, WEST]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
GOOD_CELL = "G"


def _cells_per_plus(val):
    return (val-1)*4+1


def _is_in_grid_range(x, y, grid):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)


def _is_valid_plus(cell, counter, save_directions, grid):
    """
    Determine if the cell given in parameters can grow and be a valid plus.
    Check if the plus is in the grid range and if the new crossing segments
    are good cells.

    In:
    cell (tuple(pos_x, pos_y)): current position on the grid
    counter (int): size of the crossing segment
    save_directions (set): set used to save all the intermediate plus created
                           with the given center cell
    grid (list(list)): boardgame

    Out:
    (Boolean): True if the plus can grow.
               False if the plus cannot.
    """
    tmp = set()
    for direction in DIRECTIONS:
        dir_x, dir_y = [d*counter+c for d, c in zip(direction, cell)]

        not_in_grid = not _is_in_grid_range(dir_x, dir_y, grid)

        if not_in_grid or grid[dir_y][dir_x] != GOOD_CELL:
            return False

        tmp.add((dir_x, dir_y))

    save_directions.update(tmp)
    return True


def _plus(cell, unique_pluses, grid):
    """
    Create the biggest plus possible.
    Save all the intermediate pluses in unique_pluses.

    In:
    cell (tuple(pos_x, pos_y)): current position on the grid
    unique_pluses (list(tuple(int, set))): list used to save all the pluses
                                           created with their size.
    grid (list(list)): boardgame

    Out:
    None
    """
    counter = 1
    save_directions = set([cell])

    while _is_valid_plus(cell, counter, save_directions, grid):
        counter += 1
        unique_pluses.append((_cells_per_plus(counter),
                              save_directions.copy()))


def compute_max_product(pluses):
    """
    Find the 2 biggest pluses that don't overlap. Then multiply them together.

    In:
    unique_pluses (list(tuple(int, set)))

    Out:
    (int): product of the 2 biggest pluses.
    """
    product_pluses = [(idx1, idx2, val1*val2)
                      for (idx1, (val1, _)), (idx2, (val2, _))
                      in combinations(enumerate(pluses), 2)]
    product_pluses.sort(key=lambda x: x[2], reverse=True)

    for idx1, idx2, product in product_pluses:
        if not (pluses[idx1][1] & pluses[idx2][1]):
            return product

    return max([size_plus for size_plus, _ in pluses]) if pluses else 1


# Complete the twoPluses function below.
def twoPluses(grid):
    """
    Go through the grid and for all valid cells try to construct the biggest
    plus possible. Once all the valid pluses have been build,
    it takes the two biggest pluses which doesn't overlap
    and multiply their size.

    In:
    grid (list(list)): Boardgame

    Out:
    Product of the 2 biggest pluses of the grid.
    """
    unique_pluses = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == GOOD_CELL:
                _plus((x, y), unique_pluses, grid)

    return compute_max_product(unique_pluses)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n, m = [int(val) for val in input().split()]

    grid = [input() for _ in range(n)]

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
