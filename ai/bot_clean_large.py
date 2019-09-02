#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:24:00 2019

@author: cheshirecat12
"""


DIRTY_CELL = "d"


def manhattan_dist(pos_bot, pos_dirt):
    return sum(abs(pos_b-pos_d) for pos_b, pos_d in zip(pos_bot, pos_dirt))


def next_move(pos_y, pos_x, dimx, dimy, boar):

    # Check if the bot is on a dirty cell
    if board[pos_y][pos_x] == DIRTY_CELL:
        return "CLEAN"

    dirty_cells = [(j, i)
                   for i, row in enumerate(board)
                   for j, cell in enumerate(row)
                   if cell == DIRTY_CELL]

    bot = (pos_x, pos_y)
    closest_cell = (float("INF"), None)
    for cell in dirty_cells:
        current_dist = manhattan_dist(bot, cell)
        if current_dist < closest_cell[0]:
            closest_cell = (current_dist, cell)

    _, (cell_x, cell_y) = closest_cell

    if cell_y > pos_y:
        return "DOWN"
    elif cell_y < pos_y:
        return "UP"
    elif cell_x > pos_x:
        return "RIGHT"
    else:
        return "LEFT"


# Tail starts here


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    print(next_move(pos[0], pos[1], dim[0], dim[1], board))
