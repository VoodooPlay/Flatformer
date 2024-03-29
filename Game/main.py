import pygame
import game_function as gf
from Player import Player
import game_menu


pygame.init()


font = pygame.font.Font(None, 48)

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Flatformer")

clock = pygame.time.Clock()
FPS = 60

player = Player(screen)
menu = game_menu.GameMenu(screen)

while True:
    if menu.menu_active:
        menu.main_menu()
    else:
        gf.update_screen(screen, player)
        player.update()

        player_x = font.render("str(player.player_rect.x)", True, (0, 0, 0))
        screen.blit(player_x, (100, 100))

    gf.check_events(player, menu)

    clock.tick(FPS)
