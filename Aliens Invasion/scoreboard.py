import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self, settings, screen, stats):
        """Initialize the scoreboard"""
        
        # Set the screen and screen rectangle attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set the settings and stats attributes
        self.settings = settings
        self.stats = stats
        
        # Set the text color and font for the scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score, high score, and level
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Render the score as an image"""
        
        # Round the score to the nearest 10 and format it with commas
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        
        # Render the score as an image using the font, text color, and background color
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        
        # Set the position of the score image on the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Render the high score as an image"""
        
        # Round the high score to the nearest 10 and format it with commas
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        
        # Render the high score as an image using the font, text color, and background color
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Set the position of the high score image on the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top    

    def prep_level(self):
        """Render the level as an image"""
        
        # Render the level as an image using the font, text color, and background color
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)
        
        # Set the position of the level image on the screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Prepare the ship images for display"""
        
        # Create a group to hold the ship images
        self.ships = Group()
        
        # Create ship objects based on the number of ships left in the stats
        for ship_number in range(self.stats.ship_left):
            ship = Ship(ai_settings=self.settings, screen=self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw the score, high score, level, and ship images on the screen"""
        
        # Draw the score image on the screen at its designated position
        self.screen.blit(self.score_image, self.score_rect)
        
        # Draw the high score image on the screen at its designated position
        self.screen.blit(self.high_score_image, self.high_score_rect)
        
        # Draw the level image on the screen at its designated position
        self.screen.blit(self.level_image, self.level_rect)
        
        # Draw the ship images on the screen
        self.ships.draw(self.screen)
