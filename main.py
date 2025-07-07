import pygame
import sys

from helpers import resource_path
from menu import main_menu
from gameover import game_over_screen
from snake import Snake
from food import Food

# Clock to control the frame rate
clock = pygame.time.Clock()
frame_rate = 10

# Screen variables
width = 810
height = 600
tile_size = 30

# Colors
background_color = (60, 61, 48)
grid_line_color = (70, 71, 54)
snake_color = (131, 135, 73)
food_color = (200, 50, 50)

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
icon_path = resource_path("ic_snake.png")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

def draw_grid():
    window.fill(background_color)
    for x in range(tile_size, width, tile_size):
        pygame.draw.line(window, grid_line_color, (x, 0), (x, height))
    for y in range(tile_size, height, tile_size):
        pygame.draw.line(window, grid_line_color, (0, y), (width, y))

def run_game():
    direction = 'RIGHT'
    snake = Snake(0, 0, snake_color, tile_size)
    food = Food(0, 0, food_color, tile_size)
    food.spawn(width, height, snake.body)
    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    return False  # User wants to quit

        snake.move(direction)
        head_x, head_y = snake.body[0]

        # Check for collision with window borders
        if head_x < 0 or head_x >= width // tile_size or head_y < 0 or head_y >= height // tile_size:
            return True  # Game over

        # Check if snake collides with itself
        if (head_x, head_y) in snake.body[1:]:
            return True  # Game over

        # Check if snake eats the food
        if head_x == food.x and head_y == food.y:
            food.spawn(width, height, snake.body)
            snake.grow = True

        snake.update(window)
        food.draw(window)
        pygame.display.update()
        clock.tick(frame_rate)

main_menu(window, width)
while True:
    restart = run_game()
    if not restart:
        break
    game_over_screen(window, width, height)