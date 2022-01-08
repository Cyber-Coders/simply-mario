from menu import *
import sys
import time
import config
import pygame
import pygame_gui


class Map:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass



class Game:
    def __init__(self):
        self.size = config.SIZE
        self.screen = pygame.display.set_mode(self.size)

        self.clock = pygame.time.Clock()

    def update(self):
        self.screen.fill((0, 255, 0))
        self.clock.tick(config.FPS)
        pygame.display.flip()


def game_plot():  # Сюжет игры
    screen = pygame.display.set_mode((1280, 720))
    manager = pygame_gui.UIManager((1280, 720), 'theme.json')
    clock = pygame.time.Clock()
    pygame.mixer.music.pause()
    count = 1
    running = True
    image = pygame.image.load('data/sprites/starter_template.jpg')
    button_continue = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1010, 650), (260, 55)),
                                                   text='Continue', manager=manager)

    while running:
        time_delta = clock.tick(30) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_continue:
                    count += 1

            manager.process_events(event)

        if count == 2:
            running = False
            main()

        manager.update(time_delta)
        if count == 1:
            screen.blit(image, (0, 0))

        manager.draw_ui(screen)
        pygame.display.flip()


def start_menu():  # Запуск меню
    menu = Menu()
    menu.menu()


def main():
    screen = pygame.display.set_mode((1280, 720))
    frame = 1
    frame_image = pygame.image.load(f'data/sprites/start/{frame}.png')
    screen.blit(frame_image, (0, 0))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        if frame < 24:
            frame += 1

        frame_image = pygame.image.load(f'data/sprites/start/{frame}.png')
        screen.blit(frame_image, (0, 0))

        clock.tick(config.FPS)
        pygame.display.flip()


if __name__ == "__main__":
    start_animation()
    start_menu()
