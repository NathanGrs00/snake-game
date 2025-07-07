import pygame
import sys

def wait_for_key(actions):
    import pygame
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys; sys.exit()
            if event.type == pygame.KEYDOWN:
                action = actions.get(event.key)
                if action:
                    return action()