import pygame


class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.menu_active = True
        self.SCREEN_COLOR = 'black'

    def play_button(self, x, y, width, height, text, action):
        pass

    def print_text(self, text):
        font = pygame.font.SysFont('arial', 30, bold=True)
        menu_text = font.render(text, True, 'white')
        text_width, text_height = menu_text.get_size()
        self.screen.fill(self.SCREEN_COLOR)
        self.screen.blit(menu_text, ((self.screen_rect[2] - text_width) // 2, 100))

    def main_menu(self):
        self.print_text("Menu")
        # self.play_button()
        pygame.display.flip()
