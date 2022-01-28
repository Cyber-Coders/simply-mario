import os.path
import sys
import time
import pygame
import pygame_gui
import config

from menu import Menu
from camera import Camera
from config import TILE_SIZE, W, H, FPS, TITLE, PLOT_SPRITES_PATH
from hero import Hero
from enemy_goomba import EnemyGoomba
from map import Map
from Coin import Coin

# Задаём название для окна
pygame.display.set_caption(TITLE)


# класс игры, который отображает все различные элементы и приводит для сдвига камеры для персонажа
class Game:
    def __init__(self, map_1, hero, enemy_goomba, coin_1, coin_2, coin_3, coin_4, coin_5, coin_6):
        # Задаём переменным значение
        self.map_1 = map_1
        self.hero = hero
        self.enemy_goomba = enemy_goomba
        self.coin_1 = coin_1
        self.coin_2 = coin_2
        self.coin_3 = coin_3

        self.coin_4 = coin_4
        self.coin_5 = coin_5
        self.coin_6 = coin_6

        self.camera = Camera(
            self.map_1.width * TILE_SIZE,
            self.map_1.height * TILE_SIZE)

    # Метод для отображения всех объектов в данной игре
    def render(self, screen):
        self.camera.update(self.hero)

        for row in self.map_1.blocks:
            for block in row:
                block.update(self.hero)
                screen.blit(block.image, self.camera.apply(block))

        # Отображение монет относительно карты
        screen.blit(self.enemy_goomba.image, self.camera.apply(self.enemy_goomba))
        screen.blit(self.coin_1.image, self.camera.apply(self.coin_1))
        screen.blit(self.coin_2.image, self.camera.apply(self.coin_2))
        screen.blit(self.coin_3.image, self.camera.apply(self.coin_3))

        screen.blit(self.coin_4.image, self.camera.apply(self.coin_4))
        screen.blit(self.coin_5.image, self.camera.apply(self.coin_5))
        screen.blit(self.coin_6.image, self.camera.apply(self.coin_6))

        # Отображение персонажа
        screen.blit(self.hero.image, self.camera.apply(self.hero))

        # Проверка совпадений координат монеты с игроком (Mario)
        self.coin_1.check(self.hero.get_position())
        self.coin_2.check(self.hero.get_position())
        self.coin_3.check(self.hero.get_position())

        self.coin_4.check(self.hero.get_position())
        self.coin_5.check(self.hero.get_position())
        self.coin_6.check(self.hero.get_position())

        # Методы изменяющие положение персонажа, а так же проверки совпадения координат игрока с врагом
        self.hero.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()


class Game2:
    def __init__(self, map_2, hero, enemy_goomba):
        self.map_2 = map_2
        self.hero = hero
        self.enemy_goomba = enemy_goomba

        self.enemy_goomba.rect.x = 300
        self.enemy_goomba.rect.y = 615

        self.camera = Camera(
            self.map_2.width * TILE_SIZE,
            self.map_2.height * TILE_SIZE)

    def render(self, screen):
        self.camera.update(self.hero)

        for row in self.map_2.blocks:
            for block in row:
                block.update(self.hero)
                screen.blit(block.image, self.camera.apply(block))

        screen.blit(self.hero.image, self.camera.apply(self.hero))
        screen.blit(self.enemy_goomba.image, self.camera.apply(self.enemy_goomba))

        self.hero.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()


# Метод в котором будет происходить изображение начального сюжета игры
def game_plot():
    screen = pygame.display.set_mode((W, H))
    manager = pygame_gui.UIManager((W, H), 'theme.json')

    clock = pygame.time.Clock()
    pygame.mixer.music.pause()

    plot = True
    image_num = 1
    running = True

    button_continue = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1010, 650), (260, 55)),
                                                   text='Continue', manager=manager)

    # Цикл в котором будет происходить проверка положения кнопки, а так же слайда данного сюжета
    while running:
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            # Проверка нажатия на кнопки
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_continue:
                    if image_num < 6:
                        image_num += 1

                    else:
                        plot = False

            manager.process_events(event)

        if not plot:
            running = False
            main()

        manager.update(time_delta)
        if plot:
            image = pygame.image.load(os.path.join(PLOT_SPRITES_PATH, f"template_{image_num}.jpg"))
            screen.blit(image, (0, 0))

        manager.draw_ui(screen)
        pygame.display.flip()


# Функция, которая отображает заставку нашей команды
def start_animation():
    screen = pygame.display.set_mode((W, H))
    frame = 1
    frame_image = pygame.image.load(f'data/sprites/start/{frame}.png')
    screen.blit(frame_image, (0, 0))
    clock = pygame.time.Clock()

    running = True

    # Цикл, который перебирает элементы анимации с некоторой задержкой
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

        clock.tick(FPS)
        pygame.display.flip()


def main():
    # Задаём значения переменным и объектам класса
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    pygame.mixer.music.stop()

    map_1 = Map('map_1')
    map_2 = Map('map_2')
    player = Hero((19800, 200))
    enemy_goomba = EnemyGoomba((300, 615))
    coin_1 = Coin((240, 612))
    coin_2 = Coin((272, 612))
    coin_3 = Coin((304, 612))

    coin_4 = Coin((1208, 612))
    coin_5 = Coin((1240, 612))
    coin_6 = Coin((1272, 612))
    game = Game(map_1, player, enemy_goomba, coin_1, coin_2, coin_3, coin_4, coin_5, coin_6)
    game_2 = Game2(map_2, player, enemy_goomba)

    font = pygame.font.Font('data/font/font.ttf', 30)

    running = True
    while running:
        text_health = font.render(str(f"Health:{config.health}"), True, (255, 255, 255))
        text_score = font.render(str(f"Score:{config.score}"), True, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        # Отображения всех игровых объектов
        screen.fill((0, 0, 0))
        if not config.check_map_2:
            game.render(screen)
        else:
            game_2.render(screen)
        screen.blit(text_health, (30, 30))
        screen.blit(text_score, (30, 60))
        clock.tick(FPS)
        pygame.display.flip()


# Функция, которая загружает меню и передаёт в качестве аргумента сюжет
def run():
    start_animation()
    menu = Menu()
    menu.menu(game_plot, main)


if __name__ == "__main__":
    run()
