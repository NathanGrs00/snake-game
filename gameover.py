import pygame
import sys
from helpers import wait_for_key

def game_over_screen(window, width, height):
    font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.SysFont(None, 50)
    def restart(): return True
    def quit_game(): pygame.quit(); sys.exit()
    while True:
        window.fill((40, 40, 40))
        title = font.render('Game Over', True, (200, 60, 60))
        restart_text = small_font.render('Press R to Restart', True, (180, 180, 180))
        quit_text = small_font.render('Press Q to Quit', True, (180, 180, 180))
        window.blit(title, (width // 2 - title.get_width() // 2, 180))
        window.blit(restart_text, (width // 2 - restart_text.get_width() // 2, 320))
        window.blit(quit_text, (width // 2 - quit_text.get_width() // 2, 390))
        pygame.display.update()
        if wait_for_key({pygame.K_r: restart, pygame.K_q: quit_game}):
            break