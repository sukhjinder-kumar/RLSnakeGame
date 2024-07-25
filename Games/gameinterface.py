class GameInterface:
    def get_state(self):
        """Return the current state of the game."""
        pass
    
    def get_action_space(self):
        """Return a list of possible actions."""
        pass
    
    def take_action(self, action):
        """Apply the action and update the game state."""
        pass
    
    def get_reward(self):
        """Return the reward for the agent."""
        pass
    
    def is_game_over(self):
        """Check if the game has ended."""
        pass
    def show_viz(self):
        """Displays the UI of game"""
        pass
