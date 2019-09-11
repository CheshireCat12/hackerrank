#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:33:36 2019

@author: cheshirecat12
"""

import math
import os
import random
import re
import sys
from copy import deepcopy

WIN_GAME = 1000
LOOSE_GAME = -1000
TIE_GAME = 0.1
MAX_MARK = "X"
MIN_MARK = "O"
EMPTY_CELL = "_"


def _new_board_game(board, player):
    empty_cells = [(x, y)
                   for y, row in enumerate(board)
                   for x, cell in enumerate(row)
                   if cell == EMPTY_CELL]
    #print(empty_cells)
    new_boards = list()
    for x, y in empty_cells:
        new_board = deepcopy(board)
        new_board[y][x] = player
        new_boards.append(((x, y), new_board))

    # print(new_boards)

    return new_boards


def _is_end_game(board):
    """
    The game ends if the board is full -> tie game.
    It ends if one of the two players win -> max win or min win
    """

    # Check if someone win in col or row or diag
    T_board = [col for col in zip(*board)]

    rows = [set(row) for row in board]
    cols = [set(col) for col in T_board]
    diags = [set([board[x][x] for x in range(3)]),
             set([board[x][2-x] for x in range(3)])]
    rows_cols_diags = rows + cols + diags

    #print(rows_cols_diags)

    if any(unique == {MIN_MARK} for unique in rows_cols_diags):
        return LOOSE_GAME
    elif any(unique == {MAX_MARK} for unique in rows_cols_diags):
        return WIN_GAME
    elif all(not row.intersection({EMPTY_CELL}) for row in rows):
        # print("TIEEEE")
        return TIE_GAME

    return False


def alpha_beta(board_game, alpha, beta, player):
    game_ended = _is_end_game(board_game)
    if game_ended:
        #print("endgame ", game_ended)
        return (game_ended, None)

    if player == MAX_MARK:
        best_value = (float("-INF"), None)

        for action, board in _new_board_game(board_game, MAX_MARK):
            #print("board", board)
            value, _ = alpha_beta(board, alpha, beta, MIN_MARK)
            if value > best_value[0]:
                best_value = (value, action)
            #print(best_value)

            if best_value[0] >= beta:
                break
            alpha = max(alpha, best_value[0])
        #print("----", best_value)
        return best_value
    else:
        best_value = (float("INF"), None)

        for action, board in _new_board_game(board_game, MIN_MARK):
            #print("board min", board)
            value, _ = alpha_beta(board, alpha, beta, MAX_MARK)
            #print("****", value)
            if value < best_value[0]:
                best_value = (value, action)

            if alpha >= best_value[0]:
                break
            beta = min(beta, best_value[0])
        return best_value


def nextMove(player, board_game):
    print("player", player)
    return alpha_beta(board_game, float("-INF"), float("INF"), player)[1]
    #return (0, 0) if board_game[0][0] == "_" else (1, 1)


if __name__ == '__main__':
    n = input()

    board_game = [list(input()) for _ in range(3)]

    print(*nextMove(n, board_game)[::-1], sep=" ")
