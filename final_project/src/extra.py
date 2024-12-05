
sprite_sheet_player_idle = "assets/animations/Fantasy_Warrior/Sprites/IdleBlue.png"
self.sprite_sheet_enemy_idle = "assets/animations/Fantasy_Warrior/Sprites/IdleRed.png"
sprite_sheet_player_upper = "assets/animations/Fantasy_Warrior/Sprites/UpperBlue.png"
self.sprite_sheet_enemy_upper = "assets/animations/Fantasy_Warrior/Sprites/UpperRed.png"
sprite_sheet_player_slash = "assets/animations/Fantasy_Warrior/Sprites/SlashBlue.png"
self.sprite_sheet_enemy_slash = "assets/animations/Fantasy_Warrior/Sprites/SlashRed.png"
sprite_sheet_player_overhead = "assets/animations/Fantasy_Warrior/Sprites/OverheadBlue.png"
self.sprite_sheet_enemy_overhead = "assets/animations/Fantasy_Warrior/Sprites/OverheadRed.png"
self.grunt_1 = "assets/sounds/01._damage_grunt_male.wav"
self.grunt_2 = "assets/sounds/03._damage_grunt_male.wav"
self.grunt_3 = "assets/sounds/05._damage_grunt_male.wav"
self.enemy_sword_sound = "assets/sounds/sword_thunder_sound.wav"
self.player_hit_sound ="assets/sounds/Hitmarker_sound.wav"
self.success_sound = "assets/sounds/242501__gabrielaraujo__powerupsuccess.wav"


        self.frame_width = 162   
        self.frame_height = 162  
        self.hp_font = pygame.font.Font(None, 36)
        level_font = pygame.font.Font(None, 50)
        game_over_font = pygame.font.Font(None,120)
        

        self.num_frames = {
            "idle" : 10,
            "attack" : 7
        }