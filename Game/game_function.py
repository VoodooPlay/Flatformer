import pygame
import game_menu

SCREEN_COLOR = (210, 229, 184)


def update_screen(screen, player):
    screen.fill(SCREEN_COLOR)
    player.draw()
    pygame.display.flip()


def check_events(player, menu):
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     exit()
        if event.type == pygame.MOUSEBUTTONDOWN and menu.menu_active:
            # Если был сделан клик мышью
            if menu.play_rect.collidepoint(event.pos):
                menu.is_start = False
                menu.menu_active = False
                menu.is_screen_fill = False
            if menu.exit_rect.collidepoint(event.pos):
                exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.menu_active = True
                menu.main_menu()
                menu.is_screen_fill = True
                pygame.display.flip()
            elif event.key is pygame.K_w:
                player.UP = True
            elif event.key is pygame.K_s:
                player.DOWN = True
            elif event.key is pygame.K_a:
                player.LEFT = True
            elif event.key is pygame.K_d:
                player.RIGHT = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.UP = False
            elif event.key == pygame.K_s:
                player.DOWN = False
            elif event.key == pygame.K_a:
                player.LEFT = False
            elif event.key == pygame.K_d:
                player.RIGHT = False

