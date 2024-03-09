from src.constants import *
import os
import pygame
from src.ui.button import Button
from src.ui.checkbox import Checkbox


class UI_Pygame:
    def __init__(self, board):
        self.board = board
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.rows = board.rows
        self.cols = board.cols
        self.cell_width = CELL_WIDTH

        self.player_score = 0
        self.ai_score = 0

        pygame.init()
        pygame.mixer.init()

        self.assets_path = os.path.dirname(os.path.abspath(__file__)) + "/../../assets/"

        pygame.display.set_caption("Obstruction Game")
        self.screen = pygame.display.set_mode((self.width, self.height))

        background_image = pygame.image.load(self.assets_path + "background.png").convert()
        background_image = pygame.transform.scale(background_image, (self.width, self.height))
        self.background_image = background_image


    def start_screen(self):
        center_x = self.width // 2
        center_y = self.height // 2

        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render("Obstruction Game", True, black)
        
        start_button = Button(center_x - 100, center_y + 100, 200, 100, "Start", 30, 10)
        who_starts_checkbox = Checkbox(center_x - 60, center_y + 40, 20, 20, "AI starts")

        while True:
            self.screen.fill(black)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(text, (center_x - text.get_width() // 2, center_y - text.get_height() // 2 - 50))
            start_button.draw(self.screen)
            who_starts_checkbox.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if start_button.click(event):
                    return True, who_starts_checkbox.checked
                if who_starts_checkbox.click(event):
                    who_starts_checkbox.checked = not who_starts_checkbox.checked
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False, False

    def end_screen(self, winner): 
        center_x = self.width // 2
        center_y = self.height // 2

        font = pygame.font.SysFont('Comic Sans MS', 30)
        winner_message = font.render(winner + " won!", True, black)

        font = pygame.font.SysFont('Comic Sans MS', 30)
        player_score_text = font.render("Player: " + str(self.player_score), True, black)
        ai_score_text = font.render("AI: " + str(self.ai_score), True, black)

        restart_button = Button(center_x - 100, center_y + 100, 200, 100, "Restart", 30, 10)

        while True:
            self.screen.fill(black)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(winner_message, (center_x - winner_message.get_width() // 2, center_y - winner_message.get_height() // 2 - 50))

            self.screen.blit(player_score_text, (self.width - player_score_text.get_width() - 10, 10))
            self.screen.blit(ai_score_text, (self.width - ai_score_text.get_width() - 10, 10 + player_score_text.get_height()))

            restart_button.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                if restart_button.click(event):
                    return True

    def play_click_sound(self):
        click_sound = pygame.mixer.Sound(self.assets_path + "click_sound.mp3")
        click_sound.play()

    def play_win_sound(self):
        win_sound = pygame.mixer.Sound(self.assets_path + "win_sound.mp3")
        win_sound.play()

    def play_lose_sound(self):
        lose_sound = pygame.mixer.Sound(self.assets_path + "lose_sound.mp3")
        lose_sound.play()

    def event_quit(self):
        quit_event = pygame.event.peek(pygame.QUIT)
        if quit_event:
            pygame.quit()
            return True
        return False

    def event_mouse_click(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        return False

    def mouse_click_coord(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return mouse_x, mouse_y
                

    def update_screen(self):
        self.screen.fill(black)

        self.screen.blit(self.background_image, (0, 0))

        # write the scores in the top right corner of the screen
        font = pygame.font.SysFont('Comic Sans MS', 30)
        player_score_text = font.render("Player: " + str(self.player_score), True, black)
        ai_score_text = font.render("AI: " + str(self.ai_score), True, black)
        self.screen.blit(player_score_text, (self.width - player_score_text.get_width() - 10, 10))
        self.screen.blit(ai_score_text, (self.width - ai_score_text.get_width() - 10, 10 + player_score_text.get_height()))

        self.draw_board()

        pygame.display.flip()


    def screen_to_grid(self, mouse_x, mouse_y):
        center_x = self.width // 2
        center_y = self.height // 2
        start_x = center_x - self.cell_width * self.cols // 2
        start_y = center_y - self.cell_width * self.rows // 2

        mouse_x -= start_x
        mouse_y -= start_y

        col = mouse_x // self.cell_width
        row = mouse_y // self.cell_width
        return row, col


    def draw_board(self):
        center_x = self.width // 2
        center_y = self.height // 2
        start_x = center_x - self.cell_width * self.cols // 2
        start_y = center_y - self.cell_width * self.rows // 2

        for row in range(0, self.rows + 1): # Draw horizontal lines
            pygame.draw.line(self.screen, grey, (start_x, start_y + row * self.cell_width), (start_x + self.cols * self.cell_width, start_y + row * self.cell_width), 2)
        for col in range(0, self.cols + 1): # Draw vertical lines
            pygame.draw.line(self.screen, grey, (start_x + col * self.cell_width, start_y), (start_x + col * self.cell_width, start_y + self.rows * self.cell_width), 2)

        x_image = pygame.image.load(self.assets_path + "icons8-x-100.png").convert()
        x_image = pygame.transform.scale(x_image, (self.cell_width, self.cell_width))
        o_image = pygame.image.load(self.assets_path + "icons8-o-100.png").convert()
        o_image = pygame.transform.scale(o_image, (self.cell_width, self.cell_width))

        x_image.set_colorkey(black)
        o_image.set_colorkey(black)

        for row in range(self.rows):
            for col in range(self.cols):
                symbol = self.board.get_board()[row][col]
                if symbol == 'X':
                    self.screen.blit(x_image, (start_x + col * self.cell_width, start_y + row * self.cell_width))

                elif symbol == 'O':
                    self.screen.blit(o_image, (start_x + col * self.cell_width, start_y + row * self.cell_width))
                    
                elif symbol == -1:
                    pygame.draw.rect(self.screen, yellow, (start_x + col * self.cell_width + 1, start_y + row * self.cell_width + 1,
                                                            self.cell_width - 1, self.cell_width - 1), 2)
