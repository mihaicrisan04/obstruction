import random
from copy import deepcopy


class AI:
    def __init__(self, board, piece = 'O'):
        self.board = board
        self.piece = piece

    def make_move(self):
        x, y = self.__find_move()
        self.board.place_piece(x, y, self.piece)

    def __find_move(self) -> tuple:
        # Random approach
        # while True:
        #     x = random.randint(0, self.board.rows - 1)
        #     y = random.randint(0, self.board.cols - 1)
        #     if self.board.is_valid_move(x, y):
        #         return x, y

        # Minimax approach
        _, x, y = AI.minimax(self.board, 4, True, float('-inf'), float('inf'))
        return x, y

    @staticmethod
    def minimax(board, depth, maximizing_player, alpha, beta):
        if depth == 0 or board.is_game_over():
            return board.evaluate(maximizing_player), None, None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for move in board.get_possible_moves():

                new_board = deepcopy(board)
                new_board.place_piece(move[0], move[1], 'O')
                
                eval, _, _ = AI.minimax(new_board, depth - 1, False, alpha, beta)
                
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break

            return max_eval, best_move[0], best_move[1]

        else:
            min_eval = float('inf')
            best_move = None

            for move in board.get_possible_moves():

                new_board = deepcopy(board)
                new_board.place_piece(move[0], move[1], 'X')

                eval, _, _ = AI.minimax(new_board, depth - 1, True, alpha, beta)
                
                if eval < min_eval:
                    min_eval = eval
                    best_move = move

                beta = min(beta, eval)
                if beta <= alpha:
                    break

            return min_eval, best_move[0], best_move[1]

