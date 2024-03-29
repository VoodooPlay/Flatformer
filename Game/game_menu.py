import pygame


class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.menu_active = True
        self.SCREEN_COLOR = 'black'
        self.is_start = True

    def play_button(self, text):
        play_rect1 = pygame.Rect((self.screen_rect[2] - 200) // 2, 200, 200, 100)
        play_rect2 = pygame.Rect((self.screen_rect[2] - 200) // 2, 400, 200, 100)
        font = pygame.font.Font(None, 48)
        text1 = font.render(text, True, 'white')
        text2 = font.render("Exit", True, 'white')

        pygame.draw.rect(self.screen, 'green', play_rect1)
        self.screen.blit(text1, (play_rect1.x + play_rect1.width // 2 - text1.get_width() // 2,
                                 play_rect1.y + play_rect1.height // 2 - text1.get_height() // 2))
        pygame.draw.rect(self.screen, 'green', play_rect2)
        self.screen.blit(text2, (play_rect2.x + play_rect2.width // 2 - text2.get_width() // 2,
                                 play_rect2.y + play_rect2.height // 2 - text2.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Если был сделан клик мышью
                if play_rect1.collidepoint(event.pos):
                    self.is_start = False
                    self.menu_active = False
                if play_rect2.collidepoint(event.pos):
                    exit()

    def print_text(self, text):
        font = pygame.font.Font(None, 48)
        menu_text = font.render(text, True, 'white')
        text_width, text_height = menu_text.get_size()
        self.screen.fill(self.SCREEN_COLOR)
        self.screen.blit(menu_text, ((self.screen_rect[2] - text_width) // 2, 100))

    def main_menu(self):
        self.print_text("Flatformer")
        if self.is_start:
            self.play_button("Play")
        else:
            self.play_button("Continue")
        pygame.display.flip()
