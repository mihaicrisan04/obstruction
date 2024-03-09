

class UI_Console:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        print(self.board)

    def record_move(self) -> tuple:
        while True:
            try:
                x = int(input("X: "))
                y = int(input("Y: "))
            except ValueError:
                print("Invalid input")
                continue

            if self.board.is_valid_move(x, y):
                return x, y