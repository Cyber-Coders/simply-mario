from menu import *

import sys

import config
import pygame
import pygame_gui




class Game:
    def __init__(self):
        self.size = self.width, self.height = config.SIZE
        self.screen = pygame.display.set_mode(self.size)

    def start_menu(self):
        menu = Menu()
        menu.menu()

    def start_game(self):
        clock = pygame.time.Clock()
        pygame.mixer.music.stop()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill((0, 255, 0))
            clock.tick(config.FPS)

            pygame.display.flip()

    def update(self):
        self.screen.fill((0, 255, 0))

    def window_options(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        manager = pygame_gui.UIManager((1280, 720))
        clock = pygame.time.Clock()

        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                manager.process_events(event)
            manager.update(time_delta)

            manager.draw_ui(screen)
            pygame.display.flip()

    def window_records(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        manager = pygame_gui.UIManager((1280, 720))
        clock = pygame.time.Clock()

        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                manager.process_events(event)
            manager.update(time_delta)

            manager.draw_ui(screen)
            pygame.display.flip()

    def window_help(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        manager = pygame_gui.UIManager((1280, 720))
        clock = pygame.time.Clock()

        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                manager.process_events(event)
            manager.update(time_delta)

            manager.draw_ui(screen)
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.start_menu()