from src.domain.game import Game
from src.domain.player import Player
from src.domain.ai import AI
from src.domain.board import Board
from src.ui.ui_pygame import UI_Pygame
from src.ui.ui_console import UI_Console
from src.settings import read_settings


def main():
    settings = read_settings()

    board = Board(*settings['BoardSize'])  # *(cols, rows) -> unpacking the tuple
    player = Player(board)
    ai = AI(board)
    ui = UI_Pygame(board) if settings['UI'] == 'gui' else UI_Console(board)
    game = Game(board, player, ai, ui)

    game.run_gui() if settings['UI'] == 'gui' else game.run_console()


if __name__ == "__main__":
    main()