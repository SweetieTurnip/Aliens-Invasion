import pygame
import os
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        """Initialize ship object and his starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        base_path = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(base_path, 'ship_inv.bmp')
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (80, 90))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Function to update position of ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor 
        self.rect.centerx = self.center      

    def blitme(self):
        """Draws a ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center ship on the screen"""
        self.center = self.screen_rect.centerx    
