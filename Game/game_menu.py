import pygame


class GameMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.menu_active = True
        self.SCREEN_COLOR = 'black'
        self.is_start = True
        self.play_rect = pygame.Rect((self.screen_rect[2] - 200) // 2, 200, 200, 100)
        self.exit_rect = pygame.Rect((self.screen_rect[2] - 200) // 2, 400, 200, 100)
        self.is_screen_fill = False

    def play_button(self, text):        
        font = pygame.font.Font(None, 48)
        text1 = font.render(text, True, 'white')
        text2 = font.render("Exit", True, 'white')

        # pygame.draw.rect(self.screen, 'black', self.play_rect)
        self.screen.blit(text1, (self.play_rect.x + self.play_rect.width // 2 - text1.get_width() // 2,
                                 self.play_rect.y + self.play_rect.height // 2 - text1.get_height() // 2))
        # pygame.draw.rect(self.screen, 'black', self.exit_rect)
        self.screen.blit(text2, (self.exit_rect.x + self.exit_rect.width // 2 - text2.get_width() // 2,
                                 self.exit_rect.y + self.exit_rect.height // 2 - text2.get_height() // 2))

    def print_text(self, text):
        font = pygame.font.Font(None, 48)
        menu_text = font.render(text, True, 'white')
        text_width, text_height = menu_text.get_size()
        self.screen.blit(menu_text, ((self.screen_rect[2] - text_width) // 2, 100))

    def main_menu(self):
        if not self.is_screen_fill:
            screen_surf = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
            screen_surf.fill('black')
            screen_surf.set_alpha(150)
            self.screen.blit(screen_surf, (0, 0))

        # screen_surf = pygame.Surface((self.screen_rect.width, self.screen_rect.height))
        # screen_surf.fill('black')
        # screen_surf.set_alpha(100)
        # self.screen.blit(screen_surf, (0, 0))

            self.print_text("Flatformer")
            if self.is_start:
                self.play_button("Play")
            else:
                self.play_button("Continue")

            pygame.display.flip()
