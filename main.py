import sys
import pygame

from constants import *
from classes.game import Game

# PYGAME SETUP
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")

def main():

    game = Game(screen)
    board = game.board
    ai = game.ai

    print("'g' - toggle between ai and pvp")
    print("'0' - switch to ai level 0 -> random moves")
    print("'1' - switch to ai level 1 -> unbeatable")
    print("'r' - restart the game")
    print("'p' - switches move order between player and ai")

     
    # MAIN LOOP
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # g - gamemode
                if event.key == pygame.K_g:
                    print("Switched gamemode")
                    game.change_gamemode()

                # 0 - random ai
                elif event.key == pygame.K_0:
                    if board.is_empty():
                        ai.level = 0
                        print("Changed AI to level 0")
                    else:
                        print("Can't switch mode because the board is not empty, press 'r' to restart a game")

                # 1 - smart ai
                elif event.key == pygame.K_1:
                    if board.is_empty():
                        ai.level = 1
                        print("Changed AI to level 1")
                    else:
                        print("Can't switch mode because the board is not empty, press 'r' to restart a game")
                        
                # r - restart
                elif event.key == pygame.K_r:
                    game.reset()
                    board = game.board
                    ai = game.ai

                # p - change player
                elif event.key == pygame.K_p:
                    if board.is_empty():
                        ai.player = ai.player % 2 + 1
                        print("Changed players")
                    else:
                        print("Can't switch players because the board in not empty, press 'r' to restart the game")


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE

                if board.empty_square(row, col) and game.running:
                    game.make_move(row, col)

                    if game.is_over():
                        print("Game is over press 'r' to restart")
                        game.running = False

        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            pygame.display.update()

            print("AI thinking...")

            row, col = ai.eval(board)

            game.make_move(row, col)
        
            if game.is_over():
                print("Game is over, press 'r' to restart")
                game.running = False

        pygame.display.update();

main()



