import sys

import config
import pygame
import pygame_gui


class Game:
    def __init__(self):
        self.size = self.width, self.height = config.SIZE
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.Surface((1290, 720))
        self.manager = pygame_gui.UIManager((1280, 720), 'theme.json')
        self.button_start = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 200), (150, 60)), text='Start',
                                                         manager=self.manager)
        self.button_settings = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 340), (150, 60)),
                                                            text='Settings', manager=self.manager)
        self.button_help = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 410), (150, 60)), text='Help',
                                                        manager=self.manager)
        self.button_quit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 480), (150, 60)), text='Quit',
                                                        manager=self.manager)
        self.button_records = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((800, 270), (150, 60)),
                                                           text='Records',
                                                           manager=self.manager)

    def start_game(self):
        clock = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            self.screen.fill((0, 255, 0))
            clock.tick(config.FPS)

            pygame.display.flip()

    def start_menu(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load('data/sounds/super-mario-saundtrek.mp3')
        pygame.mixer.music.play(-1)

        image = pygame.image.load('data/sprites/background.png')
        clock = pygame.time.Clock()

        running = True

        while running:
            time_delta = clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

    def update(self):
        self.screen.fill((0, 255, 0))


if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.start_menu()