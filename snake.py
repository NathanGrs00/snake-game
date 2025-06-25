import pygame

# Snake class definition
class Snake:
    # Initialize the snake with position, color, and tile size
    def __init__(self, x, y, color, tile_size):
        self.x = x
        self.y = y
        self.color = color
        # Surface is a 2D image that can be drawn on the screen, the size is the tile_size
        self.image = pygame.Surface((tile_size, tile_size))
        # Fill the surface with the snake's color
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    # Update the snake's position and draw it on the window
    def update(self, tile_size, window):
        # fill the image with the snake's color
        self.image.fill(self.color)
        # Update the rectangle's position based on the snake's coordinates
        self.rect.x = self.x * tile_size
        self.rect.y = self.y * tile_size

        # Draw the snake on the window using blit
        window.blit(self.image, self.rect)