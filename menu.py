import sys

import pygame
import pygame_gui
import time

from main import Game


def window_records():  # Раздел рекордов
    screen = pygame.display.set_mode((1280, 720))
    manager = pygame_gui.UIManager((1280, 720), 'theme.json')
    clock = pygame.time.Clock()
    running = True
    image = pygame.image.load('data/sprites/records.png')
    button_cancel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1040, 600), (190, 50)), text='Back',
                                                 manager=manager)

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_cancel:
                    running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(image, (0, 0))
        manager.draw_ui(screen)
        pygame.display.flip()


def window_help():  # Раздел помощи
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager((1280, 720), 'theme.json')
    running = True
    button_cancel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1040, 600), (190, 50)), text='Back',
                                                 manager=manager)
    image = pygame.image.load('data/sprites/help.png')
    screen.blit(image, (0, 0))

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_cancel:
                    running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            manager.process_events(event)
        manager.update(time_delta)
        screen.blit(image, (0, 0))
        manager.draw_ui(screen)
        pygame.display.flip()


class Menu(Game):  # Главное меню
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load('data/sounds/super-mario-saundtrek.mp3')
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.set_mode((1280, 720))
        self.background = pygame.Surface((1290, 720))
        self.manager = pygame_gui.UIManager((1280, 720), 'theme.json')
        self.button_start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 200), (170, 60)), text='Start',
                                                         manager=self.manager)
        self.button_records = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 270), (230, 60)),
                                                           text='Records',
                                                           manager=self.manager)
        self.button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((810, 340), (140, 60)), text='Help',
                                                        manager=self.manager)
        self.button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((810, 410), (150, 60)), text='Quit',
                                                        manager=self.manager)

    def menu(self):  # Метод отображения главного меню
        clock = pygame.time.Clock()
        image = pygame.image.load('data/sprites/background.png')

        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.button_start:
                        self.start_game()

                    if event.ui_element == self.button_quit:
                        running = False

                    if event.ui_element == self.button_records:
                        window_records()

                    if event.ui_element == self.button_help:
                        window_help()

                self.manager.process_events(event)
            self.manager.update(time_delta)
            self.screen.blit(image, (0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.flip()
