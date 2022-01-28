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

pygame.display.set_caption(TITLE)


class Game:
    def __init__(self, map_1, hero, enemy_goomba, coin_1, coin_2, coin_3):
        self.map_1 = map_1
        self.hero = hero
        self.enemy_goomba = enemy_goomba
        self.coin_1 = coin_1
        self.coin_2 = coin_2
        self.coin_3 = coin_3

        self.camera = Camera(
            self.map_1.width * TILE_SIZE,
            self.map_1.height * TILE_SIZE)

    def render(self, screen):
        self.camera.update(self.hero)

        for row in self.map_1.blocks:
            for block in row:
                block.update(self.hero)
                screen.blit(block.image, self.camera.apply(block))

        screen.blit(self.enemy_goomba.image, self.camera.apply(self.enemy_goomba))
        screen.blit(self.coin_1.image, self.camera.apply(self.coin_1))
        screen.blit(self.coin_2.image, self.camera.apply(self.coin_2))
        screen.blit(self.coin_3.image, self.camera.apply(self.coin_3))

        screen.blit(self.hero.image, self.camera.apply(self.hero))

        self.coin_1.check(self.hero.get_position())
        self.coin_2.check(self.hero.get_position())
        self.coin_3.check(self.hero.get_position())

        self.hero.update()
        self.enemy_goomba.check(self.hero.get_position())
        self.enemy_goomba.update()


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

    while running:
        time_delta = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

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


def start_animation():
    screen = pygame.display.set_mode((W, H))
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

        clock.tick(FPS)
        pygame.display.flip()


def main():
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    pygame.mixer.music.stop()

    map_1 = Map()
    player = Hero((200, 200))
    enemy_goomba = EnemyGoomba((300, 612))
    coin_1 = Coin((240, 612))
    coin_2 = Coin((272, 612))
    coin_3 = Coin((304, 612))
    game = Game(map_1, player, enemy_goomba, coin_1, coin_2, coin_3)

    font = pygame.font.Font('data/font/font.ttf', 30)

    running = True
    while running:
        text_health = font.render(str(f"Health:{config.health}"), True, (255, 255, 255))
        text_score = font.render(str(f"Score:{config.score}"), True, (255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        screen.fill((0, 0, 0))
        game.render(screen)
        screen.blit(text_health, (30, 30))
        screen.blit(text_score, (30, 60))
        clock.tick(FPS)
        pygame.display.flip()


def run():
    start_animation()
    menu = Menu()
    menu.menu(game_plot, main)


if __name__ == "__main__":
    run()
