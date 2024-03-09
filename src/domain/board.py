

class Board:
    def __init__(self, cols, rows):
        self.__cols = cols
        self.__rows = rows
        self.__board = self.__create_board()
        # left-up, up, right-up, right, right-down, down, left-down, left
        self.__di = [-1, -1, -1, 0, 1, 1, 1, 0]
        self.__dj = [-1, 0, 1, 1, 1, 0, -1, -1]

    def __create_board(self):
        board = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        return board

    def __str__(self):
        string = '\t'
        for i in range(self.__cols):
            string += '\t'+str(i)
        string += '\n\t'
        for i in range(self.__cols * 9 + 2):
            string += '-'
        string += '\n'
        for i in range(self.__rows):
            string += str(i) + '\t|'
            for j in range(self.__cols):
                string += '\t'+str(self.__board[i][j])
            string += '\t|\n'
        string += '\t'
        for i in range(self.__cols * 9 + 2):
            string += '-'
        string += '\n'
        return string

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def rows(self) -> int:
        return self.__rows

    def get_board(self) -> list:
        return self.__board

    def reset_board(self):
        self.__board = self.__create_board()

    def is_game_over(self) -> bool:
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__board[i][j] == 0:
                    return False
        return True
    
    def __is_inside_the_board(self, x, y) -> bool:
        return x >= 0 and x < self.__rows and y >= 0 and y < self.__cols

    def place_piece(self, x, y, piece):
        # mark the cell as occupied
        self.__board[x][y] = piece

        # mark the cells around the placed piece as invalid
        for d in range(8):
            if self.__is_inside_the_board(x + self.__di[d], y + self.__dj[d]):
                if self.__board[x + self.__di[d]][y + self.__dj[d]] == 0:
                    self.__board[x + self.__di[d]][y + self.__dj[d]] = -1

    def is_valid_move(self, x, y) -> bool:
        if self.__is_inside_the_board(x, y) == False:
            return False
        if self.__board[x][y] == -1 or self.__board[x][y] == 'X' or self.__board[x][y] == 'O':
            return False
        return True

    def get_possible_moves(self) -> list:
        moves = []
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__board[i][j] == 0:
                    moves.append((i, j))
        return moves

    def fill(self, b, x, y):
        b[x][y] = 1
        for d in range(8):
            if self.__is_inside_the_board(x + self.__di[d], y + self.__dj[d]):
                if self.__board[x + self.__di[d]][y + self.__dj[d]] == 0 and b[x + self.__di[d]][y + self.__dj[d]] == 0:
                    self.fill(b, x + self.__di[d], y + self.__dj[d])


    def evaluate(self, last_move) -> int:
        score = 100

        free_squares = 0

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__board[i][j] == 0:
                    free_squares += 1

        score -= free_squares

        if score == 100 and last_move == 1:
            score = -1000

        return score
