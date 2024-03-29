import pygame


class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.menu_active = True
        self.SCREEN_COLOR = 'black'

    # def play_button(self, text):
    #     button_rect = pygame.Rect(300, 200, 200, 100)
    #     font = pygame.font.Font(None, 36)
    #     text = font.render(text, True, 'white')
    #     for event in pygame.event.get():
    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             # Если был сделан клик мышью
    #             if button_rect.collidepoint(event.pos):
    #                 print('Button')
    #
    #     pygame.draw.rect(self.screen, 'black', button_rect)
    #     self.screen.blit(text, (button_rect.x + button_rect.width // 2 - text.get_width() // 2,
    #                             button_rect.y + button_rect.height // 2 - text.get_height() // 2))

    def print_text(self, text):
        font = pygame.font.SysFont('arial', 30, bold=True)
        menu_text = font.render(text, True, 'white')
        text_width, text_height = menu_text.get_size()
        self.screen.fill(self.SCREEN_COLOR)
        self.screen.blit(menu_text, ((self.screen_rect[2] - text_width) // 2, 100))

    def main_menu(self):
        self.print_text("Menu")
        # self.play_button("Play")
        pygame.display.flip()
