import pygame

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((800, 600))
# Sets the title of the window.
pygame.display.set_caption('Snake')\
# Load an icon for the window.
icon = pygame.image.load('ic_snake.png')
pygame.display.set_icon(icon)

# Make sure the window stays on the screen.
running = True
while running:
    for event in pygame.event.get():
        # Check for quit event
        if event.type == pygame.QUIT:
            running = False

    # Add a background color
    window.fill((60, 61, 48))
    pygame.display.update()
