import pygame

width = 800
height = 600
tile_size = 30

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((width, height))
# Sets the title of the window.
pygame.display.set_caption('Snake')\
# Load an icon for the window.
icon = pygame.image.load('ic_snake.png')
pygame.display.set_icon(icon)

def draw_grid(tile_size):
    # Add a background color
    window.fill((60, 61, 48))

    for x in range(tile_size, width, tile_size):
        pygame.draw.line(window, (255, 255, 255), (x, 0), (x, height))

    for y in range(tile_size, height, tile_size):
        pygame.draw.line(window, (255, 255, 255), (0, y), (width, y))


# Make sure the window stays on the screen.
running = True
while running:
    # Draw the grid
    draw_grid(tile_size)

    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()