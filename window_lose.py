import pygame
import pygame_gui
import config
import sys


def window_lose():
    screen = pygame.display.set_mode(config.SIZE)
    manager = pygame_gui.UIManager(config.SIZE, 'theme.json')
    clock = pygame.time.Clock()
    running = True

    button_cancel = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 480), (190, 50)), text='Exit',
                                                 manager=manager)

    button_restart = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 480), (240, 50)), text='Restart',
                                                  manager=manager)

    image = pygame.image.load("data/sprites/empty_background.png")

    font = pygame.font.Font('data/font/font.ttf', 50)
    text_score = font.render(str(f"You Lose!"), True, (255, 255, 255))

    screen.blit(image, (0, 0))
    screen.blit(text_score, (470, 300))

    while running:
        time_delta = clock.tick(config.FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button_cancel:
                    sys.exit()

                if event.ui_element == button_restart:
                    config.RESTART = True
                    running = False
                    config.HEALTH = 2

            manager.process_events(event)

        manager.update(time_delta)
        manager.draw_ui(screen)
        pygame.display.flip()
