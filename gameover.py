import pygame
import sys

def game_over_screen(window, width, height):
    font = pygame.font.SysFont(None, 80)
    small_font = pygame.font.SysFont(None, 50)
    game_over = True
    while game_over:
        window.fill((40, 40, 40))
        title = font.render('Game Over', True, (200, 60, 60))
        restart = small_font.render('Press R to Restart', True, (180, 180, 180))
        quit_ = small_font.render('Press Q to Quit', True, (180, 180, 180))
        window.blit(title, (width // 2 - title.get_width() // 2, 180))
        window.blit(restart, (width // 2 - restart.get_width() // 2, 320))
        window.blit(quit_, (width // 2 - quit_.get_width() // 2, 390))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_over = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()