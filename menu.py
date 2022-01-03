import pygame
import pygame_gui
import time

from main import Game


class Menu(Game):
    def __init__(self):
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
        self.button_records = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((770, 290), (230, 60)), text='Records',
                                                        manager=self.manager)
        self.button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((810, 380), (140, 60)), text='Help',
                                                        manager=self.manager)
        self.button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((810, 460), (150, 60)), text='Quit',
                                                        manager=self.manager)


    def start_menu(self):
        clock = pygame.time.Clock()
        image = pygame.image.load('data/sprites/background.png')

        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.button_start:
                        self.start_game()

                    if event.ui_element == self.button_settings:
                        self.window_options()

                    if event.ui_element == self.button_quit:
                        running = False

                    if event.ui_element == self.button_records:
                        self.window_records()

                    if event.ui_element == self.button_records:
                        self.window_help()

                self.manager.process_events(event)
            self.manager.update(time_delta)

            self.screen.blit(image, (0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.flip()


menu = Menu()
menu.start_menu()
