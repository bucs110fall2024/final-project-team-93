from src.player import Player
from src.assassin import Assassin
from src.brute import Brute
from src.knight import Knight
from src.king import King
import pygame
import pygame
import pygame_menu



class Controller:
    def __init__(self):
        """
        Initialize pygame and set up screen and other data.
        """
        pygame.init()
        pygame.event.pump()
        
        self.screen = pygame.display.set_mode()  
        # self.player = ...
        
  
    def mainloop(self):
        """
        Main game loop.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            # Detect collisions and update models
            
            self.screen.fill((0, 0, 0))  # Example: Black background
            
            # Redraw next frame 
            
            # Display next frame
            pygame.display.flip()