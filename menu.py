import sys
import pygame_gui
import sqlite3
import pygame

from config import W, H, FPS


def window_records():  # Раздел рекордов
    screen = pygame.display.set_mode((W, H))
    manager = pygame_gui.UIManager((W, H), 'theme.json')

    clock = pygame.time.Clock()
    running = True
    image = pygame.image.load('data/sprites/records.png')
    button_cancel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1040, 600), (190, 50)),
                                                 text='Back',
                                                 manager=manager)

    while running:
        time_delta = clock.tick(FPS) / 1000.0

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
    screen = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    manager = pygame_gui.UIManager((W, H), 'theme.json')
    running = True
    button_cancel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1040, 600), (190, 50)), text='Back',
                                                 manager=manager)
    image = pygame.image.load('data/sprites/help.png')
    screen.blit(image, (0, 0))

    while running:
        time_delta = clock.tick(FPS) / 1000.0

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


class Menu:  # Главное меню
    def __init__(self):
        super().__init__()
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        pygame.mixer.music.load('data/sounds/super-mario-saundtrek.mp3')
        pygame.mixer.music.play(-1)

        self.con = sqlite3.connect("BD.db")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("""SELECT display FROM Plot""").fetchall()
        self.display = self.result[0][0]

        self.screen = pygame.display.set_mode((W, H))
        self.background = pygame.Surface((W, H))
        self.manager = pygame_gui.UIManager((W, H), 'theme.json')
        self.button_start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 200), (170, 60)), text='Start',
                                                         manager=self.manager)
        self.button_records = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 270), (230, 60)),
                                                           text='Records',
                                                           manager=self.manager)
        self.button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((810, 340), (140, 60)), text='Help',
                                                        manager=self.manager)
        self.button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((810, 410), (150, 60)), text='Quit',
                                                        manager=self.manager)

    def menu(self, game_plot, game_runner):  # Метод отображения главного меню
        print(self.display)
        clock = pygame.time.Clock()
        image = pygame.image.load('data/sprites/background.png')

        running = True

        while running:
            time_delta = clock.tick(FPS) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.button_start:
                        if self.display == 0:
                            self.result = self.cur.execute("""Update Plot set display = 1""").fetchall()
                            self.con.commit()
                            self.con.close()
                            game_plot()

                        if self.display == 1:
                            game_runner()

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
