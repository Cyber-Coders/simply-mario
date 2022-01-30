import pygame
import config


def transition_menu(screen):
    screen = screen

    sound = pygame.mixer.Sound("data/sounds/button.wav")
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    menu = pygame.image.load('data/sprites/Menu.jpg')
    menu1 = menu.get_rect(
        bottomright=(800, 400))

    font = pygame.font.Font('data/font/font.ttf', 30)
    font_text1 = pygame.font.Font('data/font/font.ttf', 24)
    font_text2 = pygame.font.Font('data/font/font.ttf', 18)

    Text = font_text1.render('Congratulations', True, (0, 0, 0))
    Text_add = font_text2.render('you passed the level!', True, (0, 0, 0))

    screen.blit(menu, menu1)
    screen.blit(Text, (508, 220))
    screen.blit(Text_add, (500, 258))

    backlight_Quit = (222, 156, 14)
    backlight_Next = (222, 156, 14)

    x = 510
    y = 320

    # Проверка и изменение цвета при наведении у кнопки Quit
    if x < mouse[0] < x + 100:
        if y < mouse[1] < y + 30:
            backlight_Quit = (247, 171, 8)

            # Нажатие на кнопку Quit
            if click[0] == 1:
                pygame.mixer.Sound.play(sound)
                pygame.time.delay(1000)
                return True

    Quit = font.render('Quit', True, backlight_Quit)
    screen.blit(Quit, (x, y))

    # Проверка и изменение цвета во время наведения у кнопки Next
    if x + 170 < mouse[0] < x + 270:
        if y < mouse[1] < y + 30:
            backlight_Next = (247, 171, 8)

            # Нажатие на кнопку next
            if click[0] == 1:
                pygame.mixer.Sound.play(sound)
                pygame.time.delay(1000)
                config.check_map_2 = True

    Next = font.render('Next', True, backlight_Next)
    screen.blit(Next, (x + 170, y))
