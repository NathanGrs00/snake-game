import pygame

class Snake:
    def __init__(self, x, y, color, tile_size):
        self.body = [(x, y)]  # List of (x, y) positions
        self.color = color
        self.tile_size = tile_size
        self.grow = False

    def move(self, direction):
        head_x, head_y = self.body[0]
        if direction == 'LEFT':
            head_x -= 1
        elif direction == 'RIGHT':
            head_x += 1
        elif direction == 'UP':
            head_y -= 1
        elif direction == 'DOWN':
            head_y += 1
        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def update(self, window):
        for segment in self.body:
            rect = pygame.Rect(segment[0] * self.tile_size, segment[1] * self.tile_size, self.tile_size, self.tile_size)
            pygame.draw.rect(window, self.color, rect)