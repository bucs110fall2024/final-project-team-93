class Hp:
    def __init__(self, max_hp, x, y, font, color=(255,255,255)):
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.x = x
        self.y = y
        self.font = font 
        self.color = color
        
    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)
        
    def draw(self, screen):
        hp_value = f'HP: {self.current_hp}/{self.max_hp}'
        text_surface = self.font.render(hp_value, True, self.color)
        screen.blit(text_surface, (self.x, self.y))