import pygame
import config

from database import *

db = Database()


def transition_menu(screen):
    sound = pygame.mixer.Sound("data/sounds/button.wav")
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    menu = pygame.image.load('data/sprites/Menu.jpg')
    menu1 = menu.get_rect(
        bottomright=(800, 400))

    font = pygame.font.Font('data/font/font.ttf', 30)
    font_text1 = pygame.font.Font('data/font/font.ttf', 24)
    font_text2 = pygame.font.Font('data/font/font.ttf', 18)

    text = font_text1.render('Congratulations', True, (0, 0, 0))
    text_add = font_text2.render('you passed the level!', True, (0, 0, 0))

    screen.blit(menu, menu1)
    screen.blit(text, (508, 220))
    screen.blit(text_add, (500, 258))

    backlight = (222, 156, 14)

    x = 510
    y = 320

    # Проверка и изменение цвета при наведении у кнопки Quit
    if x < mouse[0] < x + 100:
        if y < mouse[1] < y + 30:
            backlight = (247, 171, 8)

            # Нажатие на кнопку Quit
            if click[0] == 1:
                pygame.mixer.Sound.play(sound)
                pygame.time.delay(1000)
                return True

    quit = font.render('Quit', True, backlight)
    screen.blit(quit, (x, y))

    # Проверка и изменение цвета во время наведения у кнопки Next
    if x + 170 < mouse[0] < x + 270:
        if y < mouse[1] < y + 30:
            backlight = (247, 171, 8)

            # Нажатие на кнопку next
            if click[0] == 1:
                pygame.mixer.Sound.play(sound)
                pygame.time.delay(1000)
                db.add_record(1)

                config.CHECK_MAP_2 = True
                config.SCORE = 0
                config.HEALTH = 2

    next = font.render('Next', True, backlight)
    screen.blit(next, (x + 170, y))


def level_end_transition(screen):
    sound = pygame.mixer.Sound("data/sounds/button.wav")
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    menu = pygame.image.load('data/sprites/end_background.png')

    font = pygame.font.Font('data/font/font.ttf', 30)

    screen.blit(menu, (0, 0))

    backlight = (222, 156, 14)

    x = 310
    y = 650

    # Проверка и изменение цвета при наведении у кнопки Back
    if x < mouse[0] < x + 100:
        if y < mouse[1] < y + 30:
            backlight = (247, 171, 8)

            # Нажатие на кнопку Back
            if click[0] == 1:
                pygame.mixer.Sound.play(sound)
                pygame.time.delay(1000)
                return True

    quit = font.render('Back', True, backlight)
    screen.blit(quit, (x, y))
