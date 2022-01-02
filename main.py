import sys

import config
import pygame


class Game:
    def __init__(self):
        self.size = self.width, self.height = config.SIZE
        self.screen = pygame.display.set_mode(self.size)

    def update(self):
        self.screen.fill((0, 255, 0))


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption(config.TITLE)

    game = Game()
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        game.update()
        clock.tick(config.FPS)

        pygame.display.flip()
