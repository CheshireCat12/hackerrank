#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:47:54 2019

@author: cheshirecat12

Hackerrank exercise: botclean. Receive a grid 5X5 and the bot must clean all
                               the dirty cells in the grid.

https://www.hackerrank.com/challenges/botclean/problem
"""

DIRTY_CELL = "d"


def next_move(posr, posc, board):

    # Check if the bot is on a dirty cell
    if board[posr][posc] == DIRTY_CELL:
        return "CLEAN"

    # Check if there is a dirty cell in the bot's row
    if not DIRTY_CELL in board[posr]:
        return "DOWN"

    # Check if the bot is at the right of the dirty cell
    if board[posr].index(DIRTY_CELL) > posc:
        return "RIGHT"
    else:
        return "LEFT"

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))