import pygame
from src.constants import white, grey, black, yellow


class Button:
    def __init__(self, x, y, width, height, text, font_size=20, corner_radius=5):
        self.rect_normal = pygame.Rect(x, y, width, height)
        self.rect_hovered = pygame.Rect(x - 5, y - 5, width + 10, height + 10)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.corner_radius = corner_radius
        self.hovered = False

    def draw(self, surface):
        # color = grey if self.hovered else yellow
        color = yellow
        rect = self.rect_hovered if self.hovered else self.rect_normal
        pygame.draw.rect(surface, color, rect, border_radius=self.corner_radius)
        text_surface = self.font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)

    def click(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect_hovered.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                return True
        return False