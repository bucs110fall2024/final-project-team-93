import pygame
import random
from src.hp import Hp

class Player(pygame.sprite.Sprite):
   def __init__(self, x, y, sprite_sheet_idle, sprite_sheet_upper, sprite_sheet_slash, sprite_sheet_overhead, frame_width, frame_height, num_frames, font, grunt_1, grunt_2, grunt_3):
      """
      Initialize the player with a sprite sheet.
      x: int - Starting x coordinate
      y: int - Starting y coordinate
      sprite_sheet_file: str - Path to the sprite sheet file
      frame_width: int - Width of a single frame
      frame_height: int - Height of a single frame
      num_frames: int - Total number of frames in the sprite sheet
      """
      super().__init__()
      
      self.sprite_sheets = {
         "idle": pygame.image.load(sprite_sheet_idle).convert_alpha(),
         "upper": pygame.image.load(sprite_sheet_upper).convert_alpha(),
         "slash": pygame.image.load(sprite_sheet_slash).convert_alpha(),
         "overhead": pygame.image.load(sprite_sheet_overhead).convert_alpha()
      }
      
      self.animations = {
         "idle": self.load_frames(self.sprite_sheets["idle"], frame_width, frame_height, num_frames["idle"]),
         "upper": self.load_frames(self.sprite_sheets["upper"], frame_width, frame_height, num_frames["attack"]),
         "slash": self.load_frames(self.sprite_sheets["slash"], frame_width, frame_height, num_frames["attack"]),
         "overhead": self.load_frames(self.sprite_sheets["overhead"], frame_width, frame_height, num_frames["attack"])
      }
      
      self.player_sounds = {
         "grunt_1": pygame.mixer.Sound(grunt_1),
         "grunt_2" : pygame.mixer.Sound(grunt_2),
         "grunt_3" : pygame.mixer.Sound(grunt_3),
      }


      self.current_animation = "idle"
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.is_animating = True
      self.animation_speed = 100  
      self.last_updated = pygame.time.get_ticks()
      
      
      self.image = self.frames[self.current_frame]
      self.rect = self.image.get_rect()
      self.rect.topleft = (x, y)
       
      self.can_attack = False
      self.attack_window_end = 0
      self.attacked_this_phase = False
      self.hp = Hp(100,20,20,font)
      self.current_attack = None

   def load_frames(self, sprite_sheet, frame_width, frame_height, num_frames):
      """
      Extract frames from the sprite sheet.
      frame_width: int - Width of each frame
      frame_height: int - Height of each frame
      num_frames: int - Number of frames to extract
      :return: List of frames (pygame.Surface objects)
      """
      frames = []
      sheet_width, sheet_height = sprite_sheet.get_size()
      for i in range(num_frames):
         x = (i * frame_width) % sheet_width
         y = (i * frame_width) // sheet_width * frame_height
         frame = sprite_sheet.subsurface(pygame.Rect(x, y, frame_width, frame_height))
         scaled_frame = pygame.transform.scale(frame, (frame_width*3,frame_height*3))
         frames.append(scaled_frame)
      return frames

   def update(self):
      """
      Handle sprite updates (like animations).
      """
      if self.is_animating:
         now = pygame.time.get_ticks()
         if now - self.last_updated > self.animation_speed:
               self.last_updated = now
               self.current_frame += 1
               
               if self.current_frame >= len(self.frames):
                  if self.current_animation in ["slash", "upper", "overhead"]:
                     self.current_animation = "idle"
                     self.frames = self.animations[self.current_animation]
                     self.current_frame = 0
                  else:
                     self.current_frame = 0
               
               
               self.image = self.frames[self.current_frame]

   def start_animation(self):
      """
      Start playing the animation.
      """
      self.is_animating = True

   def stop_animation(self):
      """
      Stop the animation and reset to the first frame.
      """
      self.is_animating = False
      self.current_frame = 0
      self.image = self.frames[self.current_frame]
      
   def counter(self, enemy):
      now = pygame.time.get_ticks()
      if self.can_attack and now <= self.attack_window_end:
         enemy.take_damage(10)
         self.can_attack = False
      else: 
         self.take_damage(10)
         
         
   
   def take_damage(self, damage):
      self.hp.take_damage(damage)
      self.player_sounds[random.choice(["grunt_1","grunt_2","grunt_3"])].play()
      
      
   
   def draw_health(self, screen):
      self.hp.draw(screen)
   

   def overhead(self):
      """
      Perform an overhead attack animation.
      """
      if (self.can_attack == False) or (self.attacked_this_phase == True):
         return
      self.current_attack = "overhead"
      self.current_animation = "overhead"
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.start_animation()    
      self.attacked_this_phase = True  

   def slash(self):
      """
      Perform a slash attack animation.
      """
      if (self.can_attack == False) or (self.attacked_this_phase == True):
         return
      self.current_attack = "slash"
      self.current_animation = "slash"
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.start_animation()     
      self.attacked_this_phase = True  
      
   def upper(self):
      """
      Perform a uppercut attack animation.
      """
      if (self.can_attack == False) or (self.attacked_this_phase == True):
         return
      self.current_attack = "upper"
      self.current_animation = "upper"
      self.frames = self.animations[self.current_animation]
      self.current_frame = 0
      self.start_animation()
      self.attacked_this_phase = True  
   
   def reset_attack(self):
      self.current_attack = None
      self.attacked_this_phase = False
      
   def counter(self, enemy):
      if self.current_attack == enemy.current_attack:
         enemy.take_damage(10)
         self.can_attack = False
      else: 
         self.take_damage(10)
      self.reset_attack()
      
