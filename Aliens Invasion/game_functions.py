import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ship, settings = None, screen = None, bullets = None):
    """Events that is processed when the key was pressed"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)



def check_keyup_events(event, ship):
    """Events that are processed when a key is released"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False  
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, settings, screen, bullets, stats, play_button, aliens, sb):
    """Function to check the events in the game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, settings, screen, bullets)    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)  
        elif event.type == pygame.MOUSEBUTTONDOWN:   
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Check if the play button is clicked and start a new game"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True   

        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        aliens.empty()
        bullets.empty()

        create_fleet(settings, screen, ship, aliens) 
        ship.center_ship()        

def ship_hit(settings, stats, screen, ship, aliens, bullets, sb):
    """Handles the collision between the ship and aliens"""
    if stats.ship_left > 0:
        stats.ship_left -= 1

        sb.prep_ships()

        aliens.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False 
        pygame.mouse.set_visible(True)   

def update_bullets(settings, screen, stats, sb, ship, aliens, bullets):
    """Update the position of bullets and handle bullet-alien collisions"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets)        

def check_bullet_alien_collisions(settings, screen, stats, sb, ship, aliens, bullets):
    """Check for collisions between bullets and aliens"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        # Iterate over the values (lists of aliens) in the collisions dictionary
        for aliens in collisions.values():
            stats.score += settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(settings, screen, ship, aliens)          


def fire_bullet(settings, screen, ship, bullets):
    """Fire a bullet if the limit hasn't been reached yet"""
    if len(bullets) < settings.bullets_allowed:
        new_bullet  = Bullet(settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(setting, screen, stats, ship, aliens, bullets, play_button, sb):
    """Update the screen during gameplay"""
    screen.fill(setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
            break    

def check_fleet_edges(settings, aliens):
    """Check if any aliens in the fleet have reached the edges of the screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break

def change_fleet_direction(settings, aliens):
    """Change the direction of the fleet and move it down"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1        

def update_aliens(settings, stats, screen, ship, aliens, bullets, sb):
    """Update the positions of aliens and check for collisions"""
    check_fleet_edges(settings, aliens)
    aliens.update()    
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets, sb)    

def get_number_aliens_x(settings, alien_width):
    """Calculate the number of aliens that can fit in a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(settings, screen, aliens, alien_number, row_number):
    """Create a single alien and add it to the aliens group"""
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 *alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(settings, ship_height, alien_height):
    """Calculate the number of rows that can fit on the screen"""
    available_space_y = (settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_fleet(settings, screen, ship, aliens):
    """Create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_rows(settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, screen, aliens, alien_number, row_number)

def check_high_score(stats, sb):
    """Check if the current score is a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()