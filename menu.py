import pygame
import pygame_gui

from main import Game


class Menu(Game):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.background = pygame.Surface((1290, 720))
        self.manager = pygame_gui.UIManager((1280, 720))
        self.button_start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 200), (150, 60)), text='Start',
                                                         manager=self.manager)
        self.button_settings = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 270), (150, 60)),
                                                            text='Settings', manager=self.manager)
        self.button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 340), (150, 60)), text='Help',
                                                        manager=self.manager)
        self.button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 410), (150, 60)), text='Quit',
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

                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.button_quit:
                        running = False

                self.manager.process_events(event)
            self.manager.update(time_delta)

            self.screen.blit(image, (0, 0))
            self.manager.draw_ui(self.screen)
            pygame.display.flip()