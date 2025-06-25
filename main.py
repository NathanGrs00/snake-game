import pygame

# Initialize pygame
pygame.init()

# Create a window
window = pygame.display.set_mode((800, 600))
# Sets the title of the window.
pygame.display.set_caption('Snake')

# Make sure the window stays on the screen.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


