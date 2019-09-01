#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:55:39 2019

@author: cheshirecat12

Hackerrank exercise: save princess 2. In this exercise the bot must find
                     find the princess in the given grid. Once the princess
                     position is found, the bot must move to the princess.

https://www.hackerrank.com/challenges/saveprincess2/problem
"""

PRINCESS = "p"


def nextMove(n, bot_pos_x, bot_pos_y, grid):
    princess_pos_x, princess_pos_y = [(row.find(PRINCESS), i)
                                      for i, row in enumerate(grid)
                                      if PRINCESS in row][0]
    vert = princess_pos_y - bot_pos_y
    hor = princess_pos_x - bot_pos_x

    if vert > 0:
        return "DOWN"
    elif vert < 0:
        return "UP"
    elif hor > 0:
        return "RIGHT"
    elif hor < 0:
        return "LEFT"

    return "Here I am!"


def main():
    n = int(input())
    r, c = [int(val) for val in input().strip().split()]
    grid = [input() for _ in range(n)]

    print(nextMove(n, c, r, grid))


if __name__ == "__main__":
    main()
