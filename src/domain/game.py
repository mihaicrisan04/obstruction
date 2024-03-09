import time
import sys


class Game:
    def __init__(self, board, player, ai, ui):
        self.board = board
        self.player = player
        self.ai = ai
        self.ui = ui
        self.start_player_turn = None
        self.player_turn = None
        self.player_score = 0
        self.ai_score = 0

    def run_console(self):
        while True:
            self.ui.print_board()
            print('Player turn')
            x, y = self.ui.record_move()
            self.player.make_move(x, y)
            if self.board.is_game_over():
                print('Player won!')
                break

            self.ui.print_board()
            print('AI turn')
            time.sleep(1)  # Artificial delay
            self.ai.make_move()
            if self.board.is_game_over():
                print('AI won!')
                break
        self.ui.print_board()

    def run_gui_game(self):
        running = True
        while running:
            self.ui.update_screen()

            # Check for closing the game
            if self.ui.event_quit():
                running = False
                return
            
            if self.player_turn:
                if self.ui.event_mouse_click():
                    x, y = self.ui.screen_to_grid(*self.ui.mouse_click_coord())
                    if self.board.is_valid_move(x, y):
                        self.ui.play_click_sound()
                        self.player.make_move(x, y)
                        self.player_turn = False
            else:
                # time.sleep(1)  # Artificial delay
                self.ui.play_click_sound()
                self.ai.make_move()
                self.player_turn = True

            if self.board.is_game_over():
                running = False

        # player_turn = 1 -> AI won
        # player_turn = 0 -> Player won
        winner = "AI" if self.player_turn else "Player"

        if winner == "AI":
            self.ai_score += 1
            self.ui.ai_score = self.ai_score
        else:
            self.player_score += 1
            self.ui.player_score = self.player_score

        self.ui.play_win_sound() if winner == "Player" else self.ui.play_lose_sound()

        # show the screen and wait for the user to close or restart the game
        restart = self.ui.end_screen(winner)
        if restart:
            self.board.reset_board()
            self.player_turn = self.start_player_turn
            self.run_gui_game()

    def run_gui(self):
        play, player_turn = self.ui.start_screen()
        self.start_player_turn = not player_turn
        self.player_turn = self.start_player_turn

        if play:
            self.run_gui_game()

        