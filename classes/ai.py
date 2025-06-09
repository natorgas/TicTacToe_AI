import random
import copy

class Ai:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player

    def rnd(self, board):
        empty_sqrs = board.get_empty_squares()
        idx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[idx]

    def minimax(self, board, maximizing):
        # base case
        case = board.final_state()
        
        if case == 1:
            return 1 if self.player == 2 else -1, None
        
        elif case == 2:
            return -1 if self.player == 2 else 1, None

        elif board.is_full():
            return 0, None

        if maximizing:
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_squares()
            
            for (row, col) in empty_sqrs:
                temp_board = board.clone()
                temp_board.mark_square(row, col, 1 if self.player == 2 else 2)
                eval = self.minimax(temp_board, not maximizing)[0]
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximizing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_squares()
            
            for (row, col) in empty_sqrs:
                temp_board = board.clone()
                temp_board.mark_square(row, col, 2 if self.player == 2 else 1)
                eval = self.minimax(temp_board, not maximizing)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)

            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            move = self.rnd(main_board)
            eval = 'random'

        else:
            eval, move = self.minimax(main_board, False) # AI will be the player that minimizes

        print(f"AI has chosen to mark the square in pos {move} with an eval of {eval}")

        return move # (row, col)

