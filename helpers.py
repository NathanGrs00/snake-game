import sys
import os
import pygame

def wait_for_key(actions):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys; sys.exit()
            if event.type == pygame.KEYDOWN:
                action = actions.get(event.key)
                if action:
                    return action()

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)