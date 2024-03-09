import pygame
from src.constants import white, grey, black, yellow


class Checkbox:
    def __init__(self, x, y, width, height, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = yellow
        self.checked = False
        self.label = label

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 2)  # Draw checkbox border

        if self.checked:
            pygame.draw.line(surface, self.color, self.rect.topleft, self.rect.bottomright, 2)
            pygame.draw.line(surface, self.color, self.rect.topright, self.rect.bottomleft, 2)

        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, black)
        surface.blit(text, (self.rect.x + self.rect.width + 10, self.rect.y))

    def click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False