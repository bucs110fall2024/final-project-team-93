import pygame

class Game_over:
    def __init__(self, x, y, color=(255,255,255)):
        self.x = x
        self.y = y
        self.game_over_font = pygame.font.Font(None,120)
        self.color = color
        
    def draw(self, screen):
        text  = 'Game Over'
        text_surface = self.game_over_font.render(text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))