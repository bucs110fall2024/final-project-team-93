class Level:
    def __init__(self, level, x, y, font, color=(255,255,255)):
        self.level = level
        self.x = x
        self.y = y
        self.font = font 
        self.color = color
        
        
        
    def draw(self, screen):
        level_value = f'Level: {self.level}'
        text_surface = self.font.render(level_value, True, self.color)
        screen.blit(text_surface, (self.x, self.y))