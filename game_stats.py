class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
