class Setting:
    def __init__(self):
        """Standard function for creating a object with all customizable settings"""
        #screen settings
        self.screen_width = 1200 
        self.screen_height = 800
        self.bg_color = (0, 0, 255) #blue
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):    
        """Initialize dynamic parametrs to increase difficulty of the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.alien_points = 50

        self.fleet_direction = 1

    def increase_speed(self):
        """Increases the speed of the game"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)


