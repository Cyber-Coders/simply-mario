import pygame


MOVE_SPEED = 8


class EnemyGoomba:
    def __init__(self, position):
        self.image = pygame.Surface((25, 34))
        pygame.draw.circle(
            self.image,
            (255, 255, 255),
            (self.image.get_width() // 2, self.image.get_height() // 2),
            self.image.get_width() // 2)
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

    def update(self):
        if self.rect.x < 19952:
            self.rect.x += MOVE_SPEED
        else:
            self.rect.x = 200

    def get_position(self):
        return self.rect.x, self.rect.y

