from menu import *
import sys
import time
import config
import pygame
import pygame_gui
import pytmx


# Объявление констант
TILE_SIZE = 20
SCROLL = [0, 0]


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


class Map:  # Карта
    def __init__(self, free_tiles):
        self.map = pytmx.load_pygame("data/maps/map_1.tmx")
        self.height = self.map.height
        self.width = self.map.width
        self.tile_size = self.map.tilewidth
        self.free_tiles = free_tiles

    def render(self, screen):
        for i in range(6):
            for y in range(self.height):
                for x in range(self.width):
                    image = self.map.get_tile_image(x, y, i)
                    if image is not None:
                        screen.blit(image, (x * TILE_SIZE, y * TILE_SIZE))

    def get_tile_id(self, position):
        return self.map.tiledgidmap[self.map.get_tile_gid(*position, 0)]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles


class Hero:  # Персонаж
    def __init__(self, position):
        self.x, self.y = position

    def set_postion(self, position):
        self.x, self.y = position

    def get_position(self):
        return self.x, self.y

    def render(self, screen):
        center = self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.circle(screen, (255, 255, 255), center, TILE_SIZE // 2)


class Game:  # Игра
    def __init__(self, map_1, hero):
        self.map_1 = map_1
        self.hero = hero

    def render(self, screen):
        self.map_1.render(screen)
        self.hero.render(screen)

    def update_hero(self):
        next_x, next_y = self.hero.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 1
        if self.map_1.is_free((next_x, self.hero.y)):
            self.hero.set_postion((next_x, self.hero.y))


def game_plot():  # Сюжет игры
    screen = pygame.display.set_mode((1280, 720))
    manager = pygame_gui.UIManager((1280, 720), 'theme.json')
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()
    count = 1
    running = True
    image = pygame.image.load('data/sprites/starter_template.jpg')
    button_continue = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1010, 650), (260, 55)),
                                                   text='Continue', manager=manager)

    while running:
        time_delta = clock.tick(30) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_continue:
                    count += 1

            manager.process_events(event)

        if count == 2:
            running = False
            main()

        manager.update(time_delta)
        if count == 1:
            screen.blit(image, (0, 0))

        manager.draw_ui(screen)
        pygame.display.flip()


def start_animation():  # Анимация запуска игры
    screen = pygame.display.set_mode((1280, 720))
    frame = 1
    frame_image = pygame.image.load(f'data/sprites/start/{frame}.png')
    screen.blit(frame_image, (0, 0))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if frame < 24:
            frame += 1

        frame_image = pygame.image.load(f'data/sprites/start/{frame}.png')
        screen.blit(frame_image, (0, 0))

        if frame == 24:
            time.sleep(2)
            running = False

        clock.tick(config.FPS)
        pygame.display.flip()


def start_menu():  # Запуск меню
    menu = Menu()
    menu.menu()


def main():
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    pygame.mixer.music.stop()

    map_1 = Map([i for i in range(10000)])
    player = Hero((0, 12))
    game = Game(map_1, player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        game.render(screen)
        game.update_hero()
        clock.tick(config.FPS)
        pygame.display.flip()


if __name__ == "__main__":
    start_animation()
    start_menu()