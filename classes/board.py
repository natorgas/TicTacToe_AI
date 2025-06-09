from constants import *
import numpy as np
import pygame

class Board:
    def __init__(self, screen):
        self.squares = np.zeros((ROWS, COLS))
        self.marked_sqrs = 0
        self.screen = screen

    def final_state(self, show=False):
        # return 0 if there is no win yet
        # return 1 if player 1 wins
        # return 2 if player 2 wins

        # vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(self.screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col]

        # horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(self.screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0]

        # desc diagonal
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(self.screen, color, iPos, fPos, LINE_WIDTH+5)
            return self.squares[1][1]

        # asc diagonal
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(self.screen, color, iPos, fPos, LINE_WIDTH+5)
            return self.squares[1][1]

        # no win yet
        return 0


    def mark_square(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def clone(self):
        newb = Board(self.screen)
        newb.squares = self.squares.copy()
        newb.marked_sqrs = self.marked_sqrs
        return newb

    def empty_square(self, row, col):
        return self.squares[row][col] == 0

    def is_empty(self):
        return self.marked_sqrs == 0

    def is_full(self):
       return self.marked_sqrs == 9

    def get_empty_squares(self):
        empty_squares = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_square(row, col):
                    empty_squares.append((row, col))

        return empty_squares





