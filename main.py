import sys

import pygame
import config


class Game:
    def __init__(self):
        self.size = self.width, self.height = config.SIZE
        self.screen = pygame.display.set_mode(self.size)

    def start_game(self):
        pygame.init()
        pygame.display.set_caption(config.TITLE)
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
