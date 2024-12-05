class Game_over:
    def __init__(self, x, y, font, color=(255,255,255)):
        self.x = x
        self.y = y
        self.font = font 
        self.color = color
        
    def draw(self, screen):
        text  = 'Game Over'
        text_surface = self.font.render(text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))