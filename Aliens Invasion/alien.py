import pygame
from pygame.sprite import AbstractGroup, Sprite

class Alien(Sprite):
    def __init__(self, settings, screen):
        """Init function of alien"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('/home/keyserz/Documents/Aliens Invasion/alien_ship.bmp')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Blit alien in screen"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Check if alien touch the screen edge"""
        screen_rect = self.screen.get_rect()        
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Updating position of aliens on screen"""
        self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
        self.rect.x = self.x
