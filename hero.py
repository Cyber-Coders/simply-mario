import config
from enemy_goomba import EnemyGoomba

import pygame
import pyganim
import sys

JUMP_POWER = 10
GRAVITY = 0.5
MOVE_SPEED = 8
ANIMATION_DELAY = 1

ANIMATION_STAY = [('data/sprites/hero/mario_stay.png', 1)]
ANIMATION_JUMP = [('data/sprites/hero/mario_jump.png', 1)]
ANIMATION_RIGHT = [('data/sprites/hero/mario_right1.png'),
                   ('data/sprites/hero/mario_right2.png'),
                   ('data/sprites/hero/mario_right3.png'),
                   ('data/sprites/hero/mario_right4.png'),
                   ('data/sprites/hero/mario_right5.png')]
ANIMATION_LEFT = [('data/sprites/hero/mario_left1.png'),
                  ('data/sprites/hero/mario_left2.png'),
                  ('data/sprites/hero/mario_left3.png'),
                  ('data/sprites/hero/mario_left4.png'),
                  ('data/sprites/hero/mario_left5.png')]
ANIMATION_JUMP_LEFT = [('data/sprites/hero/mario_jump_left.png', 1)]
ANIMATION_JUMP_RIGHT = [('data/sprites/hero/mario_jump_right.png', 1)]


class Hero:  # Персонаж
    def __init__(self, position):
        self.velocity_x = 0
        self.velocity_y = 0

        self.grounded = True  # переключатель для проверки возможности совершения прыжка - если grounded=False, значит игрок находится в воздухе
        self.image = pygame.Surface((25, 34))
        pygame.draw.circle(
            self.image,
            (255, 255, 255),
            (self.image.get_width() // 2, self.image.get_height() // 2),
            self.image.get_width() // 2)
        self.image.set_colorkey((0, 0, 0))

        # rect - хорошая штука, помогает проверять столкновения с другими объёктами, у которых тоже есть rect, ну и координаты хранит
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()

        self.boltAnimJump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.boltAnimJump.play()

        self.boltAnimJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play()

        self.boltAnimJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play()

        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

    def update(self):
        pressed = pygame.key.get_pressed()
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]

        if left:
            self.velocity_x = -MOVE_SPEED
            self.image.fill((0, 0, 0))
            if not self.grounded:
                self.boltAnimJumpLeft.blit(self.image, (0, 0))
            else:
                self.boltAnimLeft.blit(self.image, (0, 0))

        if right:
            self.velocity_x = MOVE_SPEED
            self.image.fill((0, 0, 0))
            if not self.grounded:
                self.boltAnimJumpRight.blit(self.image, (0, 0))
            else:
                self.boltAnimRight.blit(self.image, (0, 0))

        if not left and not right:
            self.velocity_x = 0
            if self.grounded:
                self.image.fill((0, 0, 0))
                self.boltAnimStay.blit(self.image, (0, 0))

        if pressed[pygame.K_UP]:
            if self.grounded:
                self.velocity_y -= JUMP_POWER
                self.image.fill((0, 0, 0))
                self.boltAnimJump.blit(self.image, (0, 0))
                self.grounded = False

        if self.velocity_y < 12:
            self.velocity_y += GRAVITY

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.x >= 19984:
            config.check_map_2 = True
            self.rect.x = 200
            self.rect.y = 200

    def get_position(self):
        return self.rect.x, self.rect.y
