import pygame.font

class Button():
    def __init__(self, settings, screen, msg):    
        """Initialize the Button class"""
        
        # Set the screen and screen rectangle attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and colors of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # Green
        self.text_color = (255, 255, 255)  # White
        self.font = pygame.font.SysFont(None, 48)

        # Create the button's rectangle and center it on the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare the button's message
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Render the button's message as an image"""
        
        # Render the message as an image using the specified font, text color, and button color
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        
        # Get the rectangle of the message image and center it on the button's rectangle
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw the button on the screen"""
        
        # Fill the button's rectangle with the button color
        self.screen.fill(self.button_color, self.rect)
        
        # Draw the message image on the screen, centering it within the button's rectangle
        self.screen.blit(self.msg_image, self.msg_image_rect)   