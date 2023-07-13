import pygame
from settings import Setting
import game_functions as gf
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    """Initialize the game"""
    pygame.init()
    setting = Setting()
    screen = pygame.display.set_mode((setting.screen_width, setting.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(setting, screen, "Play")
    ship = Ship(screen=screen, ai_settings=setting)
    bullets = Group()
    aliens = Group()
    stats = GameStats(setting)
    sb = Scoreboard(setting, screen, stats)
    gf.create_fleet(setting, screen, ship, aliens)
    while True:
        gf.check_events(ship, setting, screen, bullets, stats, play_button, aliens, sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(setting, screen, stats, sb, ship, aliens, bullets)   
            gf.update_aliens(setting, stats, screen, ship, aliens, bullets, sb)    
        gf.update_screen(setting, screen, stats, ship, aliens, bullets, play_button, sb)    
          

run_game()



        
