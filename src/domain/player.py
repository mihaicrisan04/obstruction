

class Player:
    def __init__(self, board, piece = 'X'):
        self.board = board
        self.piece = piece

    def make_move(self, x, y):
        if self.board.is_valid_move(x, y):
            self.board.place_piece(x, y, self.piece)