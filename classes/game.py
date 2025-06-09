import pygame
from classes.board import Board
from classes.ai import Ai
from constants import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board(self.screen)
        self.ai = Ai()
        self.player = 1
        self.gamemode = 'ai' # pvp or ai
        self.running = True
        self.make_background()
        self.show_lines()

    def reset(self):
        self.__init__(self.screen)

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def make_background(self):
        self.screen.fill(BG_COLOR)

    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_fig(row, col)
        self.next_turn()
    
    def show_lines(self):
        # vertical
        pygame.draw.line(self.screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH) 
        pygame.draw.line(self.screen, LINE_COLOR, (WIDTH-SQSIZE, 0), (WIDTH-SQSIZE, HEIGHT), LINE_WIDTH) 

        # horizontal
        pygame.draw.line(self.screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH) 
        pygame.draw.line(self.screen, LINE_COLOR, (0, HEIGHT-SQSIZE), (WIDTH, HEIGHT-SQSIZE), LINE_WIDTH) 

    def next_turn(self):
        self.player = self.player % 2 + 1

    def is_over(self):
        return self.board.final_state(show=True) != 0 or self.board.is_full()

    def draw_fig(self, row, col):
        if self.player == 1:
            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET) 
            end_desc = ((col + 1) * SQSIZE - OFFSET, (row + 1) * SQSIZE - OFFSET)

            start_asc = (col * SQSIZE + OFFSET, (row+1) * SQSIZE - OFFSET)
            end_asc = ((col+1) *  SQSIZE - OFFSET, row * SQSIZE + OFFSET)

            pygame.draw.line(self.screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
            pygame.draw.line(self.screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:
            # draw circle
            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)
            pygame.draw.circle(self.screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)





