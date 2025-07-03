import pygame
import sys

def main_menu(window, width):
    menu_running = True
    font = pygame.font.SysFont(None, 60)
    while menu_running:
        window.fill((40, 40, 40))
        title = font.render('Snake Game', True, (200, 200, 100))
        start = font.render('Press SPACE to Start', True, (180, 180, 180))
        quit_ = font.render('Press Q to Quit', True, (180, 180, 180))
        window.blit(title, (width // 2 - title.get_width() // 2, 150))
        window.blit(start, (width // 2 - start.get_width() // 2, 300))
        window.blit(quit_, (width // 2 - quit_.get_width() // 2, 400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu_running = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()