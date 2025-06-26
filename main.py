import pygame
from snake import Snake

# Clock to control the frame rate
clock = pygame.time.Clock()
# Set the frame rate
frame_rate = 10

# Screen variables
width = 810
height = 600
tile_size = 30

# Colors
background_color = (60, 61, 48)
grid_line_color = (70, 71, 54)
snake_color = (131, 135, 73)

# Initialize pygame
pygame.init()
direction = 'RIGHT'  # Initial direction of the snake

# Create a window
window = pygame.display.set_mode((width, height))
# Sets the title of the window.
pygame.display.set_caption('Snake')
# Load an icon for the window.
icon = pygame.image.load('ic_snake.png')
pygame.display.set_icon(icon)

def draw_grid():
    # Add a background color
    window.fill(background_color)

    # Vertical lines
    for x in range(tile_size, width, tile_size):
        pygame.draw.line(window, grid_line_color, (x, 0), (x, height))
    # Horizontal lines
    for y in range(tile_size, height, tile_size):
        pygame.draw.line(window, grid_line_color, (0, y), (width, y))

snake = Snake(0,0, snake_color, tile_size)

# Make sure the window stays on the screen.
running = True
while running:
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
                running = False

    # Move snake based on direction
    if direction == 'LEFT':
        snake.x -= 1
    elif direction == 'RIGHT':
        snake.x += 1
    elif direction == 'UP':
        snake.y -= 1
    elif direction == 'DOWN':
        snake.y += 1

    if snake.x < 0 or snake.x >= width // tile_size or snake.y < 0 or snake.y >= height // tile_size:
        #TODO: Implement game over logic
        running = False

    snake.update(tile_size, window)
    pygame.display.update()
    clock.tick(frame_rate)