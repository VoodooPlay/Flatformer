import pygame
from pytmx.util_pygame import load_pygame

# Инициализация Pygame и создание дисплея
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Загрузка данных карты
tmx_data = load_pygame('Materials/tmx/first_test.tmx')


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)


# Создание группы спрайтов для тайлов
tile_group = pygame.sprite.Group()

# Создание тайлов и добавление их в группу спрайтов
for layer in tmx_data.visible_layers:
    if hasattr(layer, 'data'):
        for x, y, tile in layer.tiles():
            pos = (x * tmx_data.tilewidth, y * tmx_data.tileheight)
            Tile(pos, tile).add(tile_group)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отрисовка тайлов
    screen.fill((0, 0, 0))  # Очистка экрана
    tile_group.draw(screen)  # Отрисовка тайлов

    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
