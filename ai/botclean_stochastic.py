#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:09:48 2019

@author: cheshirecat12

https://www.hackerrank.com/challenges/botcleanr/problem
"""


DIRTY_CELL = "d"


def nextMove(pos_r, pos_c, board):
    if board[pos_r][pos_c] == DIRTY_CELL:
        return "CLEAN"

    dirt_pos_r, dirt_pos_c = [(i, row.index(DIRTY_CELL))
                              for i, row in enumerate(board)
                              if DIRTY_CELL in row][0]

    if dirt_pos_r < pos_r:
        return "UP"
    elif dirt_pos_r > pos_r:
        return "DOWN"
    elif dirt_pos_c < pos_c:
        return "LEFT"
    else:
        return "RIGHT"


if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(nextMove(pos[0], pos[1], board))
