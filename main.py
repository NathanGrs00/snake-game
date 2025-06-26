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
    # Draw the grid
    draw_grid()

    snake.update(tile_size, window)

    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            running = False

    # Check for key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_q]:
        running = False
    if keys[pygame.K_LEFT]:
        snake.x -= 1
    if keys[pygame.K_RIGHT]:
        snake.x += 1
    if keys[pygame.K_UP]:
        snake.y -= 1
    if keys[pygame.K_DOWN]:
        snake.y += 1

    # Update the display
    pygame.display.update()
    clock.tick(frame_rate)