#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:26:41 2019

@author: cheshirecat12
"""

from collections import defaultdict
from math import log, sqrt
from random import choice




class MTCSNode():

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self._number_of_visits = 0.
        self._results = defaultdict(int)
        self._untried_actions = None

    @property
    def untried_actions(self):
        if self._untried_actions is None:
            self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions

    @property
    def reward(self):
        wins = self._results[self.parent.state.next_to_move]
        loses = self._results[-1*self.parent.state.next_to_move]
        return wins - loses

    @property
    def n_visits(self):
        return self._number_of_visits

    def expand(self):
        action = self.untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MTCSNode(next_state, parent=self)
        self.children.append(child_node)
        return child_node

    def is_terminal_node(self):
        return self.state.is_game_over()

    def is_fully_expanded(self):
        return not self.untried_actions

    def rollout_policy(self, moves):
        return choice(moves)

    def rollout(self):
        current_rollout_state = self.state

        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout.state.move(action)

        return current_rollout_state.game_result

    def backpropagate(self, result):
        self._number_of_visits += 1
        self._results[result] += 1
        if self.parent:
            self.parent.backpropagate(result)

    def _uct_formula(self, child, c_param=1.4):
        exploitation = child.reward/child.n_visits
        exploration = c_param*sqrt((2*log(self.n_visits)/c.n_visits))
        return exploitation + exploration

    def best_child(self, c_param=1.4):
        choices_weights = [self.uct_formula(child) for c in self.children]
        # TODO: replace np.argmax
        #return self.children[np.argmax(choices_weights)]

class MTCS():

    def __init__(self, node):
        self._root = node

    def _tree_policy(self):
        current_node = self._root
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node


    def best_action(self, n_simulation):
        for _ in range(n_simulation):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        return self.root.best_child(c_param=0.)

class Domino():

    def __init__(self, f_square, value):
        self.f_square = f_square
        self.s_square = (1, 0) if value == 1 else (0, 1)
        self.value = "v" if value == 1 else "h"

    @property
    def s_square(self):
        return self.__s_square

    @s_square.setter
    def s_square(self, )

    def __repr__(self):
        return f"Coordinate first square: {self.f_square}; "\
               f"Coordinate second square: {self.s_square}; "\
               f"Value: {self.value}"


class Domineering():

    SIZE_BOARD = 8
    PLAYER_V = 1
    PLAYER_H = -1
    PLAYERS = {"v": 1, "h": -1}
    EMPTY_CELL = "-"

    def __init__(self, board_game, player=1):
        self.board_game = board_game
        self.next_to_move = player

    @property
    def game_result(self):
        return 0

    @property
    def next_to_move(self):
        return self.__next_to_move

    @next_to_move.setter
    def next_to_move(self, player):
        if player in self.PLAYERS.values():
            self.__next_to_move = player
        else:
            self.__next_to_move = self.PLAYERS[player]

    def _is_in_range(self, cell):
        return all(0 <= val < self.SIZE_BOARD for val in cell)

    def _is_cell_empty(self, cell_y, cell_x):
        return self.board_game[cell_y][cell_x] == self.EMPTY_CELL

    def _is_legal_action(self, domino):
        is_in_range = self._is_in_range(domino.s_square)
        return is_in_range and self._is_cell_empty(*domino.s_square)

    def is_game_over(self):
        return 0

    def get_legal_actions(self):
        dominos = [Domino((y, x), self.next_to_move)
                   for y, row in enumerate(self.board_game)
                   for x, cell in enumerate(row)
                   if cell == self.EMPTY_CELL]

        actions = [domino
                   for domino in dominos
                   if self._is_legal_action(domino)]

        return actions

    def move(self, action):
        pass


def nextMove(player, board_game):
    pass

def main():
    player = input()
    board_game = [list(input())
                  for _ in range(Domineering.SIZE_BOARD)]

    game = Domineering(board_game, player)

    print(game.next_to_move)
    print(*game.get_legal_actions(),sep="\n")
    print(board_game)

if __name__ == "__main__":
    main()