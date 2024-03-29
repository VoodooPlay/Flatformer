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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.main_menu()
                if menu.menu_active:
                    menu.menu_active = False
                else:
                    menu.menu_active = True
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

