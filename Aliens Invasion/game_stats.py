class GameStats():
    def __init__(self, settings):
        """Initialize game statistics"""
        
        # Set the game settings attribute
        self.settings = settings
        
        # Reset the game statistics
        self.reset_stats()
        
        # Set the game state to inactive
        self.game_active = False
        
        # Set the initial high score to 0
        self.high_score = 0

    def reset_stats(self):
        """Reset the game statistics"""
        
        # Set the number of ships left to the ship limit specified in the settings
        self.ship_left = self.settings.ship_limit
        
        # Set the initial score and level to 0 and 1, respectively
        self.score = 0
        self.level = 1


