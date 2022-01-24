import pygame


JUMP_POWER = 8
GRAVITY = 0.3
MOVE_SPEED = 10


class Hero:  # Персонаж
    def __init__(self, position):
        self.velocity_x = 0
        self.velocity_y = 0
        self.grounded = False  # переключатель для проверки возможности совершения прыжка - если grounded=False, значит игрок находится в воздухе
        self.image = pygame.Surface((16, 16))
        pygame.draw.circle(
            self.image,
            (255, 255, 255),
            (self.image.get_width()//2, self.image.get_height()//2),
            self.image.get_width()//2)
        self.image.set_colorkey((0, 0, 0))

        # rect - хорошая штука, помогает проверять столкновения с другими объёктами, у которых тоже есть rect, ну и координаты хранит
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.x, self.rect.y = position

    def update(self):
        '''Тут, думаю, всё понятно'''
        pressed = pygame.key.get_pressed()
        self.left = pressed[pygame.K_LEFT]
        self.right = pressed[pygame.K_RIGHT]

        print(self.rect.y)

        if self.left:
            self.velocity_x = -MOVE_SPEED
        if self.right:
            self.velocity_x = MOVE_SPEED

        if not self.left and not self.right:
            self.velocity_x = 0

        if pressed[pygame.K_UP]:
            if self.grounded:
                self.velocity_y -= JUMP_POWER
                self.grounded = False

        if self.velocity_y < 12:
            self.velocity_y += GRAVITY

        if self.rect.y > 675:
            self.rect.y = 670

        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y