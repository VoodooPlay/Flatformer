import pygame
import game_function as gf
from Player import Player
import game_menu


pygame.init()


font = pygame.font.Font(None, 48)

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode()
pygame.display.set_caption("Flatformer")
pygame.display.toggle_fullscreen()

clock = pygame.time.Clock()
FPS = 60

player = Player(screen)
menu = game_menu.GameMenu(screen)
menu.main_menu()

while True:
    if menu.menu_active:
        gf.check_events(player, menu)
    else:
        gf.update_screen(screen, player)
        gf.check_events(player, menu)
        player.update()

    clock.tick(FPS)
