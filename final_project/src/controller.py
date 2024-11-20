import player
import assassin
import brute
import knight
import king
import pygame


  
class Controller:

  def __init__(self):
    #setup pygame data
    '''
    docstring
    '''
    pygame.init()
    pygame.event.pump()
        
    self.screen = pygame.display.set_mode()
    # self.player = 
  
    
  # def menuloop(self):
    
  #     #event loop

  #     #update data
    
  #     #redraw
      
  # def gameloop(self):
  #     #event loop

  #     #update data

  #     #redraw
    
  # def gameoverloop(self):
  #     #event loop

  #     #update data

  #     #redraw

def mainloop(self):
   """
   docstring
   """
   while(True): 
      
      for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               exit()

      #2. detect collisions and update models

      #3. Redraw next frame

      #4. Display next frame
      pygame.display.flip()