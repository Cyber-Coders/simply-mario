from menu import *

import sys

import config
import pygame


class Game:
    def __init__(self):
        self.size = self.width, self.height = config.SIZE
        self.screen = pygame.display.set_mode(self.size)

    def start_game(self):  # Первый уровень игры
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill((0, 255, 0))
            clock.tick(config.FPS)

            pygame.display.flip()

    def update(self):
        self.screen.fill((0, 255, 0))


def start_menu():  # Запуск меню
    menu = Menu()
    menu.menu()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    start_menu()
