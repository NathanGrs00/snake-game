import pygame
import random

class Food:
    def __init__(self, x, y, color, tile_size):
        self.x = x
        self.y = y
        self.color = color
        self.tile_size = tile_size
        self.image = pygame.Surface((tile_size, tile_size))

    def spawn(self, width, height, snake_body):
        while True:
            self.x = random.randint(0, (width // self.tile_size) - 1)
            self.y = random.randint(0, (height // self.tile_size) - 1)
            if (self.x, self.y) not in snake_body:
                break

    def draw(self, window):
        self.image.fill(self.color)
        rect = self.image.get_rect(topleft=(self.x * self.tile_size, self.y * self.tile_size))
        window.blit(self.image, rect)
