## Getting Started

This is a repository for a snake game, where the game can be played by a human or an AI bot trained using Reinforcement Learning. To get started first setup the environment. This is tested on python 3.9.6. To install the packages in a fresh environment you can use - `python3 -m venv <Environment path>`, the Environment path is nothing but the path of folder in which to install the packages. To activate, `source <Environmant Path>/bin/activate` and use `deactivate` command to revert back to base python packages. Now to install libraries do `pip3 install -r requirements.txt`.

To start the game run the `main.py` file.

## Docs

The file structure is as follows - 

```
Games
	- SnakeGame
AIAgents
	- DyanmicProgramming
main.py
```

The idea is to provide general interface for both games and AI agents so that they can interact with each other, i.e. any game and any AI can work together (instead of n^2 integrations just 2n!)

The general interface of any game is -

```python
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
```


## UML Diagram

<>

## RoadMap

- Create a snake game s.t the state, rewards are structured in a way most apt for RL agents

- Create a basic AI agent

- Create a AI agent that improves in real time using RL. Also show progress metrics like running score history, averages, etc. Present it a visual format using graphs.

- Deploy the app on some server (streamlit?), so that it easy to showcase.
