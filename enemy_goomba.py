from window_lose import window_lose

import pygame
import pyganim

import config

# Применение констант
MOVE_SPEED = 8
ANIMATION_DELAY = 1

ANIMATION_RIGHT = ['data/sprites/enemy/animation_1.png',
                   'data/sprites/enemy/animation_2.png',
                   'data/sprites/enemy/animation_3.png']


# Класс, который отображает врага
class EnemyGoomba:
    def __init__(self, position):
        # Создание холста
        self.image = pygame.Surface((25, 34))
        pygame.draw.circle(
            self.image,
            (255, 255, 255),
            (self.image.get_width() // 2, self.image.get_height() // 2),
            self.image.get_width() // 2)
        self.image.set_colorkey((0, 0, 0))

        # Задаём координаты
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

    # Метод, который перемещает врага
    def update(self):
        self.image.fill((0, 0, 0))
        self.boltAnimRight.set_colorkey((255, 255, 255))
        self.boltAnimRight.blit(self.image, (0, 0))
        if self.rect.x < 19952:
            self.rect.x += MOVE_SPEED
        else:
            self.rect.x = 200

    # Метод, который сверяет позиции героя и врага
    def check(self, position):
        if position[0] == self.rect.x and (position[1] == 606 or position[1] == 607):
            config.health -= 1

        if config.health == 0:
            window_lose()