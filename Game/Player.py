import pygame


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.player_rect = pygame.Rect(50, 50, 50, 50)
        self.score = 0
        self.speed = 10

        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False

    def update(self):
        if self.UP:
            self.player_rect.y -= self.speed
        elif self.DOWN:
            self.player_rect.y += self.speed
        elif self.LEFT:
            self.player_rect.x -= self.speed
        elif self.RIGHT:
            self.player_rect.x += self.speed
        self.move()

    def move(self):
        if self.player_rect.right > self.screen_rect.right:
            self.player_rect.right = self.screen_rect.right
        elif self.player_rect.left < self.screen_rect.left:
            self.player_rect.left = self.screen_rect.left
        elif self.player_rect.bottom > self.screen_rect.bottom:
            self.player_rect.bottom = self.screen_rect.bottom
        elif self.player_rect.top < self.screen_rect.top:
            self.player_rect.top = self.screen_rect.top

    def draw(self):
        pygame.draw.rect(self.screen, (255, 100, 100), self.player_rect)
