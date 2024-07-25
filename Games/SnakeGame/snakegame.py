import pygame
import random
from ..gameinterface import GameInterface

# Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SNAKE_SIZE = 20
FPS = 15

class SnakeGame(GameInterface):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.reset()
    
    def reset(self):
        self.snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.snake_direction = (0, 0)
        self.food = (random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                     random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
        self.score = 0
        self.game_over = False

    def get_state(self):
        return self.snake, self.snake_direction, self.food

    def get_action_space(self):
        # Actions: 0 = up, 1 = right, 2 = down, 3 = left
        return [0, 1, 2, 3]

    def take_action(self, action):
        # Update direction based on action
        if action == 0 and self.snake_direction != (0, SNAKE_SIZE):  # up
            self.snake_direction = (0, -SNAKE_SIZE)
        elif action == 1 and self.snake_direction != (-SNAKE_SIZE, 0):  # right
            self.snake_direction = (SNAKE_SIZE, 0)
        elif action == 2 and self.snake_direction != (0, -SNAKE_SIZE):  # down
            self.snake_direction = (0, SNAKE_SIZE)
        elif action == 3 and self.snake_direction != (SNAKE_SIZE, 0):  # left
            self.snake_direction = (-SNAKE_SIZE, 0)

        if not self.game_over:
            # Move snake
            new_head = (self.snake[0][0] + self.snake_direction[0],
                        self.snake[0][1] + self.snake_direction[1])
            self.snake = [new_head] + self.snake[:-1]

            # Check for collisions
            if self.snake[0] == self.food:
                self.snake.append(self.snake[-1])  # Grow snake
                self.food = (random.randint(0, (SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE,
                             random.randint(0, (SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE)
                self.score += 1

            if (self.snake[0][0] < 0 or self.snake[0][0] >= SCREEN_WIDTH or
                self.snake[0][1] < 0 or self.snake[0][1] >= SCREEN_HEIGHT or
                len(self.snake) != len(set(self.snake))):  # Collides with itself or border
                self.game_over = True

    def get_reward(self):
        if self.game_over:
            return -10
        return 1 if self.snake[0] == self.food else 0

    def is_game_over(self):
        return self.game_over

    def show_viz(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        for segment in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food[0], self.food[1], SNAKE_SIZE, SNAKE_SIZE))
        pygame.display.flip()
        self.clock.tick(FPS)

# Example usage
if __name__ == "__main__":
    game = SnakeGame()
    while not game.is_game_over():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.reset()

        # Example action: move right
        game.take_action(1)
        game.show_viz()

    pygame.quit()

