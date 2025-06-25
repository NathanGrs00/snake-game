import pygame

# Screen variables
width = 810
height = 600
tile_size = 30

# Colors
background_color = (60, 61, 48)
grid_line_color = (70, 71, 54)

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

# Make sure the window stays on the screen.
running = True
while running:
    # Draw the grid
    draw_grid()

    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()