import pygame

class Level:
    def __init__(self, level, x, y, color=(255,255,255)):
        self.level = level
        self.x = x
        self.y = y
        self.level_font = pygame.font.Font(None, 50) 
        self.color = color
        
        
        
    def draw(self, screen):
        level_value = f'Level: {self.level}'
        text_surface = self.level_font.render(level_value, True, self.color)
        screen.blit(text_surface, (self.x, self.y))