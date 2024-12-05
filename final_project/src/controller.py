from src.player import Player
from src.enemy import Enemy
from src.level import Level
from src.gameover import Game_over
import pygame

class Controller:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("The Last Vanguard")
        pygame.mixer.init()
        
        self.screen_width = 988
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.background = pygame.image.load("assets/animations/background4.jpg")

        self.num_frames = {
            "idle" : 10,
            "attack" : 7
        }


        self.player = Player(100, 0)
        self.enemy = Enemy(425,0)
        self.level = Level(1,430,20)
        self.game_over = Game_over(270,140)
        self.respawn_time = None

        self.mysprites = pygame.sprite.Group()
        self.mysprites.add(self.player)
        self.mysprites.add(self.enemy)
        self.is_player_dead = False
        
        
        

    def mainloop(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:  
                        self.player.slash()
                    elif event.key == pygame.K_k:  
                        self.player.overhead()
                    elif event.key == pygame.K_l: 
                        self.player.upper()
            
            if self.is_player_dead == False:
                
                now = pygame.time.get_ticks()
                if self.player.hp.current_hp == 0:
                    self.is_player_dead = True
                
                if self.enemy.is_enemy_dead and self.respawn_time == None:
                    self.respawn_time = now + 4000
                if self.respawn_time and now >= self.respawn_time:
                    self.level.level += 1
                    new_animation_speed = self.enemy.animation_speed
                    new_attack_timer_max = self.enemy.attack_timer_max
                    self.enemy = Enemy(425,0)
                    self.enemy.animation_speed = new_animation_speed
                    self.enemy.attack_timer_max = new_attack_timer_max
                    self.enemy.attack_duration = self.enemy.animation_speed * self.num_frames["attack"]
                    self.mysprites.add(self.enemy)
                    self.respawn_time = None
                    
                    
                    
                if self.enemy.is_attacking:
                    now = pygame.time.get_ticks()
                    attack_window_start = self.enemy.attack_start_time
                    attack_window_end = self.enemy.attack_start_time + self.enemy.attack_duration
                    if attack_window_start <= now <= attack_window_end:
                        self.player.can_attack = True
                    
                    if now > attack_window_end and not self.enemy.dealt_damage:
                        if self.player.attacked_this_phase:
                            self.player.counter(self.enemy)
                        else:
                            self.player.take_damage(10)
                        self.enemy.dealt_damage = True            
                else:
                    self.player.can_attack = False
                    self.player.attacked_this_phase = False

                
                self.mysprites.update()

            self.screen.fill((0,0,0))
            
            if self.is_player_dead == False:
                self.screen.blit(self.background, (0, 0))
                self.player.draw_health(self.screen)
                self.enemy.draw_health(self.screen)
                self.mysprites.draw(self.screen)
            else:
                self.game_over.draw(self.screen)
            self.level.draw(self.screen)

            pygame.display.flip()
            clock.tick(60)
