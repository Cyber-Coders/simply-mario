from menu import *

import sys

import config
import pygame
import pygame_gui


def start_menu():
    menu = Menu()
    menu.menu()


class Game:
    def __init__(self):
        self.size = self.width, self.height = config.SIZE
        self.screen = pygame.display.set_mode(self.size)

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            pygame.mixer.music.stop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill((0, 255, 0))
            clock.tick(config.FPS)

            pygame.display.flip()

    def update(self):
        self.screen.fill((0, 255, 0))


if __name__ == "__main__":
    pygame.init()
    game = Game()
    start_menu()