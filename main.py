from menu import *

import sys

import config
import pygame
import pygame_gui


class Game:
    def __init__(self):
        pass


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
        manager.update(time_delta)
        if count == 1:
            screen.blit(image, (0, 0))

        manager.draw_ui(screen)
        pygame.display.flip()


def start_menu():  # Запуск меню
    menu = Menu()
    menu.menu()


def main():
    pygame.init()
    start_menu()
    size = config.SIZE
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 255, 0))
        clock.tick(config.FPS)
        pygame.display.flip()


if __name__ == "__main__":
    main()
